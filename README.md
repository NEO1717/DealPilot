# ✈️ DealPilot 優惠導航員 (Powered by Lemonade)

> 專為大學生打造的 AI 優惠精算師，基於 **Lemonade 本地推理架構** 與 RAG 技術，提供高隱私、低延遲的「商品 + 支付」最佳化建議。

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Architecture](https://github.com/lemonade-sdk/lemonade)
![LlamaIndex](https://img.shields.io/badge/AI-LlamaIndex-purple)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-green.svg)
## 💡 專案亮點

**DealPilot** 是展現現代 AI 應用架構的最佳範例，它整合了先進的本地推理與檢索技術：

1.  **🍋 Lemonade 架構驅動 (Local Runtime)**：
    * 本專案採用 **Lemonade** 本地 LLM 運行環境，無需將敏感對話數據上傳至雲端，確保絕對的**資料隱私**。
    * 透過 Lemonade 的 OpenAI-Compatible API，實現極低延遲的推理響應。
2. **🔍 兩階段精準檢索 (Two-Stage Retrieval)**：
    * **Step 1**: 先檢索最相關的「商品優惠」(Product Retrieval)。
    * **Step 2**: 鎖定檢索到的店家，進行二次「支付優惠」檢索 (Payment Retrieval)，確保支付方式與店家完全對應。

## 📂 專案結構

* `UI.py`: Streamlit 前端介面，包含串流處理與標籤過濾邏輯。
* `Rag_workflow.py`: 核心 RAG 工作流，實作了與 Lemonade Server 的串接。
* `Main.py`: 程式入口，負責初始化 Cache 與 Workflow。
* `knowledge_base.py`: 知識庫建置工具，整合各大超商 (全家/7-11/萊爾富/路易莎) 資料。
* `Main_knowledgeBase.dir`: 存放各家商店的優惠資訊，以結構化資料形式儲存，後續將被向量化。
* `AppConfig.py`: (需自行建立) 系統參數設定檔。
 ---
## 🚀 快速開始 (Quick Start)

### 1. 安裝環境
請確保您已安裝 Python 3.10 或以上版本。

```bash
git clone [https://github.com/你的帳號/DealPilot.git](https://github.com/你的帳號/DealPilot.git)
cd DealPilot
pip install -r requirements.txt
````

### 2. 設定 Lemonade 連線配置
本專案預設連接至本地的 Lemonade Server。請將範例設定檔改名並編輯：

```bash
# Windows
copy AppConfig_example.py AppConfig.py
# Mac/Linux
cp AppConfig_example.py AppConfig.py
```
打開 AppConfig.py，確認以下設定以適配 Lemonade 架構：
```bash
# AppConfig.py

# 1. 指向 Lemonade 本地伺服器
LLM_API_BASE = "http://localhost:8000/api/v1"  # Lemonade 預設端口

# 2. 設定專屬識別鑰 (Lemonade 架構通關密語)
LLM_API_KEY = "lemonade" 

# 3. 指定模型名稱 (需與 Lemonade 啟動的模型一致)
LLM_MODEL_NAME = "DeepSeek-R1-Distill-Llama-8B-Hybrid"
```
🔰 提示：請確保您的 Lemonade Server 已經在背景啟動 (Port 8000)，並已載入 DeepSeek 或其他兼容模型。

### 3. 建置知識庫
執行knowledge_base.py  第一次執行時，系統會自動檢查索引。：
```bash
python knowledge_base.py
```

### 4. 啟動應用
執行主程式，開啟網頁介面：
```bash
streamlit run Main.py
```
---
### 🛠️ 技術堆疊 (Tech Stack)
* Runtime: Lemonade (Local LLM Server)
* LLM: DeepSeek-R1-Distill-Llama-8B
* Embedding: BAAI/bge-m3
* Framework: LlamaIndex Workflow (Event-Driven)
* Frontend: Streamlit (Async Support)
* Tools: OpenCC (繁簡轉換)
---
### 📜License
[MIT](https://choosealicense.com/licenses/mit/)

---
## ❤️ 致謝 (Acknowledgements)

特別感謝 [Lemonade](https://github.com/這裡填寫Lemonade的正確網址) 專案提供強大的本地推理架構。
本專案 (DealPilot) 的核心推理能力由 Lemonade 驅動，實現了高隱私與低延遲的 AI 應用場景。

Special thanks to the **Lemonade** team for their amazing Local LLM Runtime.
DealPilot relies on Lemonade for its core inference capabilities, enabling a high-privacy and low-latency AI experience.
