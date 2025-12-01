from llama_index.core.schema import TextNode
from typing import List


def get_familymart_nodes() -> List[TextNode]:
    nodes = [
        # --- 會員與點數制度 (Membership/Points) ---
        TextNode(
            text="全家會員優惠【生日好咖禮】。活動期間：2025/11/28 至 2025/12/31。生日當月會員可獲得 Let's Café 大杯特濃美式免費兌換券 (冰/熱皆可)。每位會員限兌換一次。",
            metadata={
                "store_name": "FamilyMart (全家)",
                "category": "會員與點數制度",
                "topic": "會員生日咖啡",
                "keywords": ["生日", "會員", "咖啡", "特濃美式", "免費"],
                "valid_start": "2025-11-28",
                "valid_end": "2025-12-31"
            }
        ),
        TextNode(
            text="全家會員優惠【中獎發票購物金 10% 加碼】。於全家 APP 或門市使用載具領取中獎發票，可額外獲得中獎金額 10% 的全家購物金，可折抵多數商品。",
            metadata={
                "store_name": "FamilyMart (全家)",
                "category": "會員與點數制度",
                "topic": "發票購物金 10% 加碼",
                "keywords": ["發票", "購物金", "10%", "回饋", "會員"],
                "valid_start": "長期有效",
                "valid_end": "長期有效"
            }
        ),
        TextNode(
            text="全家會員優惠【台新點數自動轉 Fa 點】。活動期間：2025/07/24 至 2025/12/31。綁定台新信用卡並啟用自動轉換，可享 4% 台新點數自動轉 Fa 點，每月可轉入上限為 250 點。",
            metadata={
                "store_name": "FamilyMart (全家)",
                "category": "會員與點數制度",
                "topic": "台新點數轉換",
                "keywords": ["台新", "Fa點", "點數", "4%", "信用卡"],
                "valid_start": "2025-07-24",
                "valid_end": "2025-12-31"
            }
        ),
        TextNode(
            text="全家會員【FamiPoint 點數兌換】。FamiPoint 可用於兌換飲品、零食、生活用品、寄杯、折價券或限定商品，兌換品項依 APP 兌換專區即時更新內容為準。",
            metadata={
                "store_name": "FamilyMart (全家)",
                "category": "會員與點數制度",
                "topic": "FamiPoint 點數兌換",
                "keywords": ["FamiPoint", "點數", "兌換", "寄杯", "折價券"],
                "valid_start": "長期有效",
                "valid_end": "長期有效"
            }
        ),
        TextNode(
            text="全家會員【FamiPoint 點數折抵】。結帳可直接折抵消費，折抵比率為 300 點折 1 元，多數商品可使用。",
            metadata={
                "store_name": "FamilyMart (全家)",
                "category": "會員與點數制度",
                "topic": "FamiPoint 點數折抵",
                "keywords": ["FamiPoint", "折抵", "點數", "省錢"],
                "valid_start": "長期有效",
                "valid_end": "長期有效"
            }
        ),

        # --- 鮮食與組合優惠 (Fresh Food/Combos) ---
        TextNode(
            text="全家鮮食優惠【湯圓優惠】。活動期間：2025/11/26 至 2025/12/09。指定湯圓任選兩件 8 折、三件 75 折，品項包含芝麻、花生、黑糖、鮮肉湯圓、桂冠湯圓等貼標品項。",
            metadata={
                "store_name": "FamilyMart (全家)",
                "category": "鮮食與組合優惠",
                "topic": "湯圓優惠",
                "keywords": ["湯圓", "折扣", "鮮食", "75折", "冬季"],
                "valid_start": "2025-11-26",
                "valid_end": "2025-12-09"
            }
        ),
        TextNode(
            text="全家鮮食優惠【餐餐超值配】。鮮食搭配指定飲品享 39/49/59/69 元組合價。鮮食包含飯糰、壽司、三明治、漢堡、麵包、甜點等；飲品包含咖啡、牛奶、豆漿、茶飲等。部分飲品可加價升級。",
            metadata={
                "store_name": "FamilyMart (全家)",
                "category": "鮮食與組合優惠",
                "topic": "39-69元超值配",
                "keywords": ["超值配", "鮮食", "飯糰", "三明治", "咖啡", "組合價", "省錢"],
                "valid_start": "長期有效",
                "valid_end": "長期有效"
            }
        ),
        TextNode(
            text="全家鮮食優惠【麵包+飲品共享優惠】。購買貼標麵包可搭配指定飲品享 49 或 59 元組合價。麵包包含奶酥、巧克力麵包、菠蘿、可頌等；飲品包含牛乳、豆奶、午后時光、瓶裝咖啡等。",
            metadata={
                "store_name": "FamilyMart (全家)",
                "category": "鮮食與組合優惠",
                "topic": "麵包飲品優惠",
                "keywords": ["麵包", "飲品", "49元", "59元", "組合價"],
                "valid_start": "長期有效",
                "valid_end": "長期有效"
            }
        ),
        TextNode(
            text="全家鮮食優惠【主副配】。購買貼標主餐 (便當、焗烤、義大利麵、湯品等) 可加價 5 元搭配副餐 (飯糰、手卷、麵包、甜點等)，或加價 10 元搭配指定飲品 (牛乳、豆漿、茶飲等)。",
            metadata={
                "store_name": "FamilyMart (全家)",
                "category": "鮮食與組合優惠",
                "topic": "主副配",
                "keywords": ["主餐", "副餐", "飲品", "便當", "加價購"],
                "valid_start": "長期有效",
                "valid_end": "長期有效"
            }
        ),

        # --- 咖啡優惠 (Coffee Offers) ---
        TextNode(
            text="全家咖啡優惠【Let's Café 經典/特濃咖啡第二杯 7 折】。同品項兩杯享第二杯 7 折。適用品項：經典美式、經典拿鐵、特濃美式、特濃拿鐵 (冰/熱)。寄杯可使用；不得跨品項混搭。",
            metadata={
                "store_name": "FamilyMart (全家)",
                "category": "咖啡優惠",
                "topic": "咖啡第二杯7折",
                "keywords": ["咖啡", "Let's Café", "7折", "寄杯", "美式", "拿鐵"],
                "valid_start": "長期有效",
                "valid_end": "長期有效"
            }
        ),

        # --- 金融與支付優惠 (Finance/Payment) ---
        TextNode(
            text="全家支付優惠【悠遊付 8% 回饋】。活動期間：2025/10/01 至 2025/12/31。使用悠遊付於全家付款可享最高 8% 回饋 (基本 5% + 任務加碼 3%)。",
            metadata={
                "store_name": "FamilyMart (全家)",
                "category": "金融與支付優惠",
                "topic": "悠遊付 8% 回饋",
                "keywords": ["悠遊付", "回饋", "電子支付", "8%", "行動支付"],
                "valid_start": "2025-10-01",
                "valid_end": "2025-12-31"
            }
        ),
        TextNode(
            text="全家支付優惠【台新 Pay x Richart 卡 3.8% 回饋】。活動期間：2025/09/01 至 2025/12/31。使用台新 Pay 綁定 Richart 卡於全家付款可享基本 0.5% + 加碼 3.3% = 3.8% 回饋，需使用 Pay 著刷模式結帳。",
            metadata={
                "store_name": "FamilyMart (全家)",
                "category": "金融與支付優惠",
                "topic": "台新 Pay 3.8% 回饋",
                "keywords": ["台新 Pay", "Richart", "回饋", "3.8%", "信用卡"],
                "valid_start": "2025-09-01",
                "valid_end": "2025-12-31"
            }
        ),
        TextNode(
            text="全家支付優惠【Pi 錢包綁玉山卡 5% 回饋】。活動期間：2025/04/16 至 2026/02/28。使用 Pi 錢包綁定玉山 Pi 拍錢包信用卡於全家付款可享最高 5% 回饋，部分加碼需事前登錄。",
            metadata={
                "store_name": "FamilyMart (全家)",
                "category": "金融與支付優惠",
                "topic": "Pi 錢包 5% 回饋",
                "keywords": ["Pi錢包", "玉山卡", "回饋", "5%", "信用卡"],
                "valid_start": "2025-04-16",
                "valid_end": "2026-02-28"
            }
        ),
        TextNode(
            text="全家支付優惠【MyFamiPay 支付優惠】。使用 MyFamiPay 綁定合作銀行信用卡付款可享 3%~8% 回饋。每週三為會員支付日，鮮食、飲料或咖啡享專屬加碼優惠，部分商品享 MyFamiPay 專屬組合價或寄杯折扣。",
            metadata={
                "store_name": "FamilyMart (全家)",
                "category": "金融與支付優惠",
                "topic": "MyFamiPay 優惠",
                "keywords": ["FamiPay", "支付", "回饋", "會員支付日", "寄杯折扣", "信用卡"],
                "valid_start": "長期有效",
                "valid_end": "長期有效"
            }
        )
    ]
    return nodes


if __name__ == "__main__":
    all_familymart_nodes = get_familymart_nodes()
    print(f"成功載入 {len(all_familymart_nodes)} 個 TextNode。")

    print("\n--- 抽查節點範例 ---")

    # 範例 1: 鮮食組合
    print(f"[範例1] {all_familymart_nodes[6].text}")
    print(f"Metadata: {all_familymart_nodes[6].metadata}\n")

    # 範例 2: 會員點數
    print(f"[範例2] {all_familymart_nodes[4].text}")
    print(f"Metadata: {all_familymart_nodes[4].metadata}\n")

    # 範例 3: 支付優惠
    print(f"[範例3] {all_familymart_nodes[13].text}")
    print(f"Metadata: {all_familymart_nodes[13].metadata}\n")