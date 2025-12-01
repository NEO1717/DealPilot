import streamlit as st
import asyncio

from Rag_workflow import DealPilotWorkflow
from UI import DealPilotUI


try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)


# 2. 初始化核心引擎 (使用 @st.cache_resource)
# cache_resource 會把這個物件存在記憶體裡，下次直接拿來用。

@st.cache_resource(show_spinner="正在啟動 AI 核心引擎...")
def get_workflow_engine():
    """
    只會執行一次，負責初始化 Workflow 並確保索引就緒。
    """
    print("[Main] 初始化 Workflow Engine")

    # 實例化 Workflow (觸發模型載入)
    workflow = DealPilotWorkflow()

    # 確保索引已經建立 (如果沒有，會自動執行 ingest)
    # 使用 loop.run_until_complete 因為這裡是同步環境呼叫非同步方法
    loop.run_until_complete(workflow.ensure_ingested())

    return workflow


def main():
    """主程式入口"""

    # A. 獲取核心邏輯實例 (Model/Service)
    # 這裡會檢查 Cache，如果已經有了就直接回傳，不會重跑
    workflow_engine = get_workflow_engine()

    # B. 初始化介面實例 (View)
    # 這裡我們把 workflow_engine 和 loop "注入" (Inject) 給 UI
    app_ui = DealPilotUI(workflow=workflow_engine, loop=loop)

    # C. 啟動介面
    app_ui.run()


if __name__ == "__main__":
    main()