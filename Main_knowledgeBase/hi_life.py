from llama_index.core.schema import TextNode
from typing import List


def get_hilife_nodes_final_categorized_v2() -> List[TextNode]:
    nodes = [
        # --- A. 咖啡與寄杯優惠 (Hi-Café) ---
        TextNode(
            text="萊爾富優惠【指定咖啡買 1 送 1】。活動期間：2025/11/26 至 2025/12/23。同品項冰熱皆可，但冰熱不可混搭。買 1 送 1 品項包含：大摩卡咖啡、大醇脆黑糖拿鐵、大橙香拿鐵、中橙香美式。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "咖啡與寄杯優惠",
                "topic": "指定咖啡買1送1",
                "keywords": ["買1送1", "咖啡","摩卡咖啡", "黑糖拿鐵", "橙香拿鐵", "Hi Café"],
                "valid_start": "2025-11-26",
                "valid_end": "2025-12-23"
            }
        ),
        TextNode(
            text="萊爾富優惠【特濃咖啡寄杯優惠】。活動期間：2025/11/26 至 2025/12/23。須於 Hi-Life VIP App 購買。特濃美式大杯 (冰/熱) 買 20 杯送 20 杯。特濃拿鐵大杯 (冰/熱) 買 20 杯送 18 杯。贈送杯數須於 2026/02/28 前兌換。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "咖啡與寄杯優惠",
                "topic": "特濃咖啡寄杯優惠",
                "keywords": ["咖啡","20送20", "20送18", "特濃美式", "特濃拿鐵", "寄杯", "Hi-Life VIP"],
                "valid_start": "2025-11-26",
                "valid_end": "2025-12-23"
            }
        ),
        TextNode(
            text="萊爾富優惠【特濃拿鐵/特大拿鐵第二杯 5 元】。活動期間：2025/11/26 至 2025/12/23。指定兩款咖啡同品項冰/熱任選，第二杯僅需 5 元。適用品項：特濃拿鐵 (大杯)、特大拿鐵 (特大杯)。可使用於寄杯。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "咖啡與寄杯優惠",
                "topic": "特濃拿鐵第二杯5元",
                "keywords": ["咖啡","第二杯5元", "特濃拿鐵", "特大拿鐵", "咖啡優惠", "省錢"],
                "valid_start": "2025-11-26",
                "valid_end": "2025-12-23"
            }
        ),

        # --- B. 主餐與組合優惠 (Meal/Combo) ---
        TextNode(
            text="萊爾富優惠【熱麵霸到】。活動期間：2025/11/26 至 2025/12/23。主餐 (韓式部隊鍋、紅燒牛三寶麵、排骨雞湯麵、蔥燒切仔麵) 搭配任一指定商品 (飲品或小點) 可現折 10 元。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "主餐與組合優惠",
                "topic": "熱麵霸到折10元",
                "keywords": ["熱麵", "部隊鍋", "排骨湯麵", "折10元", "午餐"],
                "valid_start": "2025-11-26",
                "valid_end": "2025-12-23"
            }
        ),
        TextNode(
            text="萊爾富優惠【巷仔內台味便當】。活動期間：2025/11/26 至 2025/12/23。台味便當主餐 (烤黑豬飯、瓜仔肉飯、魯肉飯、滷油肉飯) 搭配指定飲品可現折 10 元 (限同筆消費)。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "主餐與組合優惠",
                "topic": "台味便當折10元",
                "keywords": ["台味便當", "魯肉飯", "烤黑豬", "折10元", "晚餐"],
                "valid_start": "2025-11-26",
                "valid_end": "2025-12-23"
            }
        ),
        TextNode(
            text="萊爾富優惠【早餐 2.0 組合價】。活動期間：2025/11/26 至 2025/12/23。每日 06:00-09:00 限定早餐組合價 49 元。其他時段合購價 59 元。主餐 (三明治/漢堡/三角飯糰) 搭配指定飲品 (豆漿/鮮乳/咖啡)。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "主餐與組合優惠",
                "topic": "早餐49元組合",
                "keywords": ["早餐49元", "三明治", "三角飯糰", "咖啡", "省錢", "限時"],
                "valid_start": "2025-11-26",
                "valid_end": "2025-12-23"
            }
        ),

        # --- C. 主題商品優惠 (Topic Promo) ---
        TextNode(
            text="萊爾富【巧級喜歡你 - 麵包優惠】。活動期間：2025/11/26 至 2025/12/23。全 12 項巧克力麵包任選 2 件 39 元。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "主題商品優惠",
                "topic": "巧克力麵包39元",
                "keywords": ["巧克力", "麵包39元", "甜點", "銅板價"],
                "valid_start": "2025-11-26",
                "valid_end": "2025-12-23"
            }
        ),
        TextNode(
            text="萊爾富【巧級喜歡你 - 零食/飲料折扣】。活動期間：2025/11/26 至 2025/12/23。巧克力零食系列任 3 件 75 折。指定 600ml 以下飲料任 2 件 8 折。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "主題商品優惠",
                "topic": "零食/飲料折扣",
                "keywords": ["巧克力", "零食", "飲料", "75折", "8折"],
                "valid_start": "2025-11-26",
                "valid_end": "2025-12-23"
            }
        ),
        TextNode(
            text="萊爾富【阿華田限量優惠】。活動期間：2025/11/26 至 2025/12/23。阿華田冰飲 (大杯，含巧克力/草莓) 特價 25 元。阿華田摩卡咖啡特價 45 元。其他合作飲品 (芋泥歐蕾等) 特價 45 元。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "主題商品優惠",
                "topic": "阿華田特價",
                "keywords": ["阿華田", "25元", "45元", "草莓阿華田", "飲品優惠"],
                "valid_start": "2025-11-26",
                "valid_end": "2025-12-23"
            }
        ),
        TextNode(
            text="萊爾富【恐龍冰沙】冬季限定。活動期間：2025/11/26 至 2025/12/23。雙杯組合 2 杯 99 元 (平均 49.5 元)。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "主題商品優惠",
                "topic": "恐龍冰沙2杯99元",
                "keywords": ["冰沙", "兩杯99元", "冬季限定", "甜品"],
                "valid_start": "2025-11-26",
                "valid_end": "2025-12-23"
            }
        ),
        TextNode(
            text="萊爾富【冬季限定熱甜湯】。玉米濃湯 45 元，上市日期 2025/12/01 起。燒仙草 45 元，上市日期 2025/12/05 起。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "主題商品優惠",
                "topic": "玉米濃湯/燒仙草45元",
                "keywords": ["燒仙草", "玉米濃湯", "45元", "冬季限定", "熱食", "新品"],
                "valid_start": "2025-12-01",
                "valid_end": "2026-03-31"
            }
        ),

        # --- D. 金融與支付優惠 (Finance/Pay) ---
        TextNode(
            text="萊爾富【聯邦 New New Bank 開戶禮】金融合作活動。活動期間：2025/10/01 至 2025/12/31。成功開戶贈送 200 元萊爾富購物金 (需綁定 Hi-Life VIP App)。活存利率最高 10%。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "金融與支付優惠",
                "topic": "New New Bank 開戶禮",
                "keywords": ["New New Bank", "購物金200", "10%活存", "開戶禮"],
                "valid_start": "2025-10-01",
                "valid_end": "2025-12-31"
            }
        ),
        TextNode(
            text="萊爾富【信用卡合作優惠】。包含聯邦、玉山、中信、台新等銀行。玉山銀行：綁定 Hi-Life Pay 享 3%~5% 加碼回饋。中信 LINE Pay 卡：LINE Pay 付款享 1%~3% LINE POINTS 回饋。台新銀行：綁定悠遊付/街口支付享 3%~6% 回饋。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "金融與支付優惠",
                "topic": "信用卡回饋",
                "keywords": ["信用卡優惠", "玉山銀行", "LINE Pay卡", "街口支付", "長期有效"],
                "valid_start": "長期有效",
                "valid_end": "長期有效"
            }
        ),
        TextNode(
            text="萊爾富【行動支付與 H-Coin 制度】。LINE Pay、街口支付、悠遊付皆有回饋。H-Coin 點數制度：1 元=1 點，50 點折 5 元，點數可折抵/兌換商品。行動支付回饋與 H-Coin 點數多數可同時疊加。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "金融與支付優惠",
                "topic": "行動支付與H-Coin",
                "keywords": ["LINE Pay", "街口支付", "悠遊付", "Hi-Life Pay", "H-Coin", "點數回饋", "長期有效"],
                "valid_start": "長期有效",
                "valid_end": "長期有效"
            }
        ),

        # --- E. 會員與預購 (Member/Preorder) ---
        TextNode(
            text="萊爾富【Hi-Life VIP 會員制度】。提供咖啡寄杯、點數累積、專屬優惠券與支付回饋等功能。會員專屬電子券不定期更新，包含飯糰、冰品、咖啡等折扣券。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "會員與預購",
                "topic": "Hi-Life VIP 會員制度",
                "keywords": ["會員限定", "點數累積", "電子券", "咖啡優惠", "VIP任務", "長期有效"],
                "valid_start": "長期有效",
                "valid_end": "長期有效"
            }
        ),
        TextNode(
            text="萊爾富優惠【TEAM TAIWAN 3D 一卡通】第二波預購。預購期間：2025/11/26 至 2026/01/05。限量 3D 立體造型一卡通。早鳥價 550 元。",
            metadata={
                "store_name": "Hi-Life 萊爾富",
                "category": "會員與預購",
                "topic": "TEAM TAIWAN 一卡通預購",
                "keywords": ["一卡通", "3D造型卡", "早鳥550", "限量預購", "週邊商品"],
                "valid_start": "2025-11-26",
                "valid_end": "2026-01-05"
            }
        )
    ]
    return nodes


if __name__ == "__main__":
    all_hilife_nodes = get_hilife_nodes_final_categorized_v2()
    print(f"成功載入 {len(all_hilife_nodes)} 個 TextNode。")

    print("\n--- 抽查節點範例 ---")

    # 範例 1: 咖啡優惠
    print(f"[範例1] {all_hilife_nodes[0].text}")
    print(f"Metadata: {all_hilife_nodes[0].metadata}\n")

    # 範例 2: 主餐優惠
    print(f"[範例2] {all_hilife_nodes[3].text}")
    print(f"Metadata: {all_hilife_nodes[3].metadata}\n")

    # 範例 3: 金融優惠
    print(f"[範例3] {all_hilife_nodes[12].text}")
    print(f"Metadata: {all_hilife_nodes[12].metadata}\n")