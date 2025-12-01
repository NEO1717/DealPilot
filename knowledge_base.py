from llama_index.core.schema import TextNode
from typing import List
from Main_knowledgeBase.FamilyMart import get_familymart_nodes
from Main_knowledgeBase.hi_life import get_hilife_nodes_final_categorized_v2
from Main_knowledgeBase.louisa import get_louisa_nodes
from Main_knowledgeBase.MOS_Burger import get_mos_burger_nodes
# from Main_knowledgeBase.seven_eleven import get_student_discount_nodes

def get_all_student_nodes() -> List[TextNode]:
    """
    整合所有商店的優惠資料，一次回傳給 Index 建立索引
    """
    all_nodes = []

    # print("正在載入 7-ELEVEN 資料...")
    # # 請確保 seven_eleven.py 已經放入資料夾，且函數名稱正確
    # all_nodes.extend(get_student_discount_nodes())

    print("正在載入 FamilyMart 資料...")
    all_nodes.extend(get_familymart_nodes())

    print("正在載入 Hi-Life 資料...")
    # 函數名稱要確認與 hi_life.py 內定義的一致
    all_nodes.extend(get_hilife_nodes_final_categorized_v2())

    print("正在載入 Louisa 資料...")
    # 函數名稱要確認與 louisa.py 內定義的一致 (原本可能是 get_kumamon_card_nodes，記得改)
    all_nodes.extend(get_louisa_nodes())

    print("正在載入 MOS Burger 資料...")
    # 函數名稱要確認與 MOS_Burger.py 內定義的一致
    all_nodes.extend(get_mos_burger_nodes())

    print(f"--- 資料載入完成，共 {len(all_nodes)} 筆優惠節點 ---")
    return all_nodes


if __name__ == "__main__":
    print("--- 開始測試資料載入 ---")

    # 這裡才是真正去「呼叫」上面定義好的函數
    nodes = get_all_student_nodes()

    # 驗證一下拿到了多少資料
    print(f"\n✅ 測試成功！總共合併了 {len(nodes)} 筆優惠資料。")

    # (選用) 隨機印出一筆來檢查看看
    if len(nodes) > 0:
        print(f"第一筆資料範例：{nodes[45].text[:1000]}...")