import os
import nest_asyncio
from typing import List, Optional
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.settings import Settings
from llama_index.core.workflow import Event, Context, Workflow, StartEvent, StopEvent, step
from llama_index.core.schema import NodeWithScore
from llama_index.core.llms import ChatMessage
from llama_index.core.base.response.schema import StreamingResponse
from llama_index.core.vector_stores import MetadataFilters, MetadataFilter
from llama_index.llms.openai_like import OpenAILike
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from AppConfig import AppConfig
from knowledge_base import get_all_student_nodes

nest_asyncio.apply()


class RetrieverEvent(Event):
    """檢索完成事件，攜帶檢索到的節點 (Nodes)"""
    nodes: List[NodeWithScore]


class DealPilotWorkflow(Workflow):
    """
    優惠規劃師的核心 RAG WORKFLOW。
    """

    def __init__(self, timeout: float = 300.0, verbose: bool = False):
        super().__init__(timeout=timeout, verbose=verbose)
        self._initialize_models()
        self.index = self._load_index_from_disk()

    def _initialize_models(self) -> None:
        self.llm = OpenAILike(
            model=AppConfig.LLM_MODEL_NAME,
            api_base=AppConfig.LLM_API_BASE,
            api_key=AppConfig.LLM_API_KEY,
            is_chat_model=True,
            timeout=AppConfig.LLM_TIMEOUT,
            max_tokens=4096
        )

        self.embed_model = HuggingFaceEmbedding(
            model_name=AppConfig.EMBEDDING_MODEL_NAME,
            device=AppConfig.EMBEDDING_DEVICE
        )

        Settings.llm = self.llm
        Settings.embed_model = self.embed_model

    def _load_index_from_disk(self) -> Optional[VectorStoreIndex]:
        persist_path = os.path.join(AppConfig.STORAGE_DIR, AppConfig.DOCSTORE_FILE)
        if os.path.exists(persist_path):
            print(f"--- [RAG Service] 發現現有索引，正在載入: {AppConfig.STORAGE_DIR} ---")
            storage_context = StorageContext.from_defaults(persist_dir=AppConfig.STORAGE_DIR)
            return load_index_from_storage(storage_context)
        else:
            print(f"--- [RAG Service] 未發現索引，等待初始化 (Ingest) ---")
            return None

    @step
    async def ingest(self, ctx: Context, ev: StartEvent) -> StopEvent | None:
        query = ev.get("query")
        if query:
            return None

        print("--- [RAG Service] 開始建立新索引... ---")
        nodes = get_all_student_nodes()
        self.index = VectorStoreIndex(nodes=nodes)
        self.index.storage_context.persist(persist_dir=AppConfig.STORAGE_DIR)
        print(f"--- [RAG Service] 索引建立完成，共 {len(nodes)} 個節點 ---")
        return StopEvent(result=self.index)

    @step
    async def retrieve(self, ctx: Context, ev: StartEvent) -> RetrieverEvent | None:
        query = ev.get("query")
        if not query:
            return None
        if self.index is None:
            raise ValueError("索引尚未初始化！請先執行 ensure_ingested()。")

        print(f"--- [RAG Service] 正在檢索使用者需求：{query} ---")

        # 階段一：商品檢索
        product_retriever = self.index.as_retriever(similarity_top_k=7)
        product_nodes = await product_retriever.aretrieve(query)

        found_stores_ordered = []
        seen_stores = set()
        for node in product_nodes:
            store = node.node.metadata.get("store_name")
            if store and store not in seen_stores:
                found_stores_ordered.append(store)
                seen_stores.add(store)

        # 階段二：支付檢索
        payment_nodes_candidates = []
        payment_query_str = "支付 信用卡 回饋 悠遊付 LINE Pay 街口 銀行 錢包"

        for store_name in found_stores_ordered:
            filters = MetadataFilters(filters=[MetadataFilter(key="store_name", value=store_name)])
            store_payment_retriever = self.index.as_retriever(filters=filters, similarity_top_k=1)
            store_payments = await store_payment_retriever.aretrieve(payment_query_str)

            for p_node in store_payments:
                cat = p_node.node.metadata.get("category", "")
                if any(k in cat for k in ["支付", "金融", "信用卡", "錢包", "Pay", "銀行", "會員"]):
                    payment_nodes_candidates.append(p_node)

        # 合併結果
        final_nodes = []
        seen_ids = set()
        for node in product_nodes:
            if node.node.node_id not in seen_ids:
                final_nodes.append(node)
                seen_ids.add(node.node.node_id)

        payment_limit = 3
        payment_count = 0
        for p_node in payment_nodes_candidates:
            if payment_count >= payment_limit:
                break
            if p_node.node.node_id not in seen_ids:
                final_nodes.append(p_node)
                seen_ids.add(p_node.node.node_id)
                payment_count += 1

        await ctx.store.set("user_query", query)
        return RetrieverEvent(nodes=final_nodes)

    @step
    async def synthesize(self, ctx: Context, ev: RetrieverEvent) -> StopEvent:
        nodes = ev.nodes
        user_query = await ctx.store.get("user_query")

        store_map = {}
        for node_score in nodes:
            text = node_score.node.get_content()
            meta = node_score.node.metadata
            store_name = meta.get("store_name", "其他商店")
            category = meta.get("category", "")

            if store_name not in store_map:
                store_map[store_name] = {'products': [], 'payments': []}

            info_str = f"- {text}"
            is_payment = any(k in category for k in ["支付", "金融", "信用卡", "錢包", "Pay", "銀行", "會員"])

            if is_payment:
                store_map[store_name]['payments'].append(info_str)
            else:
                store_map[store_name]['products'].append(info_str)

        context_list = []
        for store, data in store_map.items():
            if data['products'] or data['payments']:
                section = f"### 店家：{store}\n"
                section += "【商品/餐點優惠】:\n" + (
                    "\n".join(data['products']) if data['products'] else "(本次檢索無相關商品)") + "\n"
                section += "【支付/刷卡回饋】:\n" + (
                    "\n".join(data['payments']) if data['payments'] else "(資料庫中無此店家特定支付優惠)") + "\n"
                context_list.append(section)

        full_context_str = "\n".join(context_list)
        user_content = AppConfig.USER_MESSAGE_TEMPLATE.format(context_str=full_context_str, query_str=user_query)

        messages = [
            ChatMessage(role="system", content=AppConfig.PLANNER_SYSTEM_PROMPT),
            ChatMessage(role="user", content=user_content)
        ]

        response_gen = await self.llm.astream_chat(messages=messages)
        streaming_response = StreamingResponse(response_gen=response_gen, source_nodes=nodes)
        return StopEvent(result=streaming_response)

    async def run_query(self, query_text: str):
        return await self.run(query=query_text)

    async def ensure_ingested(self):
        if self.index is not None:
            return
        await self.run()