import os


class AppConfig:
    """
    系統設定檔範本
    【使用說明】：下載後請將此檔案重新命名為 'AppConfig.py' 並填入您的設定。
    """

    # 1. 模型設定
    LLM_MODEL_NAME = "DeepSeek-R1-Distill-Llama-8B-Hybrid"

    # 請填入您的 API Endpoint 與 Key
    LLM_API_BASE = "http://localhost:8000/api/v1"
    LLM_API_KEY = "YOUR_API_KEY_HERE"  # <--- 請使用者自行填入
    LLM_TIMEOUT = 300.0

    # Embedding 模型
    EMBEDDING_MODEL_NAME = "BAAI/bge-m3"
    EMBEDDING_DEVICE = "cpu"

    # 2. 檢索與儲存設定
    STORAGE_DIR = "./student_saver_index"
    DOCSTORE_FILE = "docstore.json"
    RETRIEVAL_TOP_K = 10

    # 3. 系統提示詞
    PLANNER_SYSTEM_PROMPT = """
你是一個貼心、懂得變通的「大學生省錢助手」。你的任務是根據提供的【優惠情報】，為使用者分析不同情境下的最佳消費選擇。

**核心規則 (違反將受罰)：**
1. **絕對誠實**：所有商品價格、回饋趴數、支付方式，**必須完全引用**提供的資料。
2. **嚴格對應**：在「執行方案」中，支付方式必須與該商品的店家一致。
3. **情境導向**：請根據不同需求，提供2種不同的「情境建議」。

**思考流程 (<think>)：**
1. **掃描**：閱讀資料，識別符合需求的商品與對應支付。
2. **分類**：思考這幾個方案分別適合什麼樣的人？
3. **撰寫**：將思考結果轉化為下列格式。

**回應格式 (Markdown)：**
(此處省略重複格式，請保留原始 Prompt)
"""

    # 4. 使用者訊息模板
    USER_MESSAGE_TEMPLATE = """
---
**目前的優惠情報 (RAG 檢索結果)：**
{context_str}
---
**您的需求：**
{query_str}
---
**你的省錢建議：**
"""