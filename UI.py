import streamlit as st
import opencc


class DealPilotUI:
    """
    負責處理 Streamlit 的畫面渲染與互動
    """

    def __init__(self, workflow, loop):
        """
        初始化 UI
        """
        self.workflow = workflow
        self.loop = loop
        # 初始化繁簡轉換器
        self.cc = opencc.OpenCC('s2t')

    def init_page(self):
        """設定頁面標題與 Layout"""
        st.set_page_config(page_title="DealPilot 大學生省錢助手", layout="wide")
        st.title("DealPilot 大學生省錢助手 🎓")
        st.caption("專為大學生打造高CP值消費計畫 (資料來源：全家/萊爾富/路易莎/摩斯/7-11)")

    def init_session_state(self):
        """初始化對話紀錄"""
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def render_chat_history(self):
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if message["role"] == "assistant" and "sources" in message:
                    with st.expander("🔎 查看參考的優惠來源"):
                        for i, node in enumerate(message["sources"]):
                            st.info(
                                f"**來源 {i + 1} (相關性: {node.score:.4f})**\n\n"
                                f"{node.node.get_content()}\n\n"
                                f"*Metadata: {node.node.metadata}*"
                            )

    async def _stream_handler(self, response_gen):
        """
        1. 防止提取到 <think> 區塊內資訊。
        2. 強制等待思考結束後，才開始尋找正文關鍵字。
        """
        buffer = ""
        is_thinking = False
        has_started_content = False

        # 定義正文開始的特徵
        start_markers = ["省錢情報", "商品優惠", "支付優惠", "💰", "💡", "###"]

        async for chunk in response_gen:
            delta_text = None
            if isinstance(chunk, str):
                delta_text = chunk
            elif hasattr(chunk, 'delta') and chunk.delta is not None:
                delta_text = chunk.delta
            elif isinstance(chunk, dict) and 'delta' in chunk and chunk['delta']:
                delta_text = chunk['delta']

            if not delta_text:
                continue

            buffer += delta_text


            if "<think>" in buffer:
                is_thinking = True

            if "</think>" in buffer:
                parts = buffer.split("</think>")
                buffer = parts[-1]
                is_thinking = False

                has_started_content = False
                continue

            if is_thinking:
                continue

            if not has_started_content:
                for marker in start_markers:
                    if marker in buffer:
                        has_started_content = True
                        start_idx = buffer.find(marker)
                        valid_content = buffer[start_idx:]

                        yield self.cc.convert(valid_content)
                        buffer = ""
                        break

                if len(buffer) > 500 and "--- 資料" not in buffer:
                    if "<think>" not in buffer:
                        has_started_content = True
                        yield self.cc.convert(buffer)
                        buffer = ""

            else:
                if buffer:
                    yield self.cc.convert(buffer)
                    buffer = ""

        if buffer and not is_thinking:
            if "--- 資料" not in buffer:
                yield self.cc.convert(buffer)

    def handle_user_input(self):
        """處理使用者輸入與 AI 回應流程"""
        if prompt := st.chat_input("請輸入你的需求（例如：我現在想喝咖啡，哪家最划算？...）"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            try:
                with st.spinner("正在幫你計算最高 CP 值方案..."):
                    async def run_query():
                        return await self.workflow.run_query(prompt)

                    result = self.loop.run_until_complete(run_query())

                    with st.chat_message("assistant"):
                        response_content = st.write_stream(
                            self._stream_handler(result.response_gen)
                        )

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response_content,
                        "sources": result.source_nodes
                    })

                    with st.expander("🔎 剛剛參考的優惠來源"):
                        for i, node in enumerate(result.source_nodes):
                            st.info(
                                f"**來源 {i + 1} (相關性: {node.score:.4f})**\n\n"
                                f"{node.node.get_content()}\n\n"
                                f"*Metadata: {node.node.metadata}*"
                            )

            except Exception as e:
                st.error(f"查詢時發生錯誤：{e}")
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"系統發生錯誤：{e}"
                })

    def run(self):
        self.init_page()
        self.init_session_state()
        self.render_chat_history()
        self.handle_user_input()