from llama_index.core.schema import TextNode
from typing import List


def get_louisa_nodes() -> List[TextNode]:

    nodes = [

        TextNode(
            text="Louisa Coffee 路易莎【11-12月黑卡會員獨享優惠】。活動期間：2025/11/01 至 2025/12/31。憑黑卡消費享多重折扣。1. 咖啡飲品：每日上午 11:00 前，第二杯 5 折（不含手沖、超越精品、冰沙）。2. 點數兌換：憑黑卡點數 5 點可換任一飲品 9 折優惠。3. 咖啡豆優惠：咖啡豆（1/4磅、半磅）單包 75 折、1/4磅兩包 7 折。4. 濾掛咖啡：任選 2 盒以上總金額 5 折。5. 週邊商品：陶瓷塗層系列享 85 折。",
            metadata={
                "store_name": "路易莎 Louisa Coffee",
                "category": "會員優惠",
                "topic": "黑卡11-12月折扣",
                "keywords": ["黑卡", "第二杯半價","咖啡", "咖啡豆", "濾掛", "買一送一", "寄杯", "早鳥優惠"],
                "valid_start": "2025-11-01",
                "valid_end": "2025-12-31"
            }
        ),
        TextNode(
            text="Louisa Coffee 路易莎 X 乾杯燒肉【極上燒肉祭】加碼延長。活動期間：即日起 至 2025/12/31。聯名新品包含：職人匠製燒牛日式飯糰、乾杯秘醬濃香燒牛飯、厚醬燒牛磚壓。特別優惠：購買上述聯名品項集滿 3 張貼紙，於活動期間至「乾杯燒肉居酒屋」消費，即享伊比利霜降豬或日本和牛炎肉買一送一。",
            metadata={
                "store_name": "路易莎 Louisa Coffee",
                "category": "新品上市",
                "topic": "極上燒肉祭",
                "keywords": ["乾杯", "燒肉", "飯糰", "磚壓", "午餐", "肉食", "買一送一"],
				"valid_start": "2025-10-13",
                "valid_end": "2025-12-31"
            }
        ),
        TextNode(
            text="Louisa Coffee 路易莎【LINE Pay 週週領優惠】。活動期間：2025/10/01 至 2025/12/31。使用 LINE Pay 單筆消費滿 120 元，即可於 LINE Pay 好康地圖領取「早餐咖啡 10 元優惠券」。每週限領一次，數量有限領完為止。",
            metadata={
                "store_name": "路易莎 Louisa Coffee",
                "category": "支付優惠",
                "topic": "LINE Pay折價券",
                "keywords": ["LINE Pay", "行動支付", "滿額贈", "10元", "早餐", "省錢"],
                "valid_start": "2025-10-01",
                "valid_end": "2025-12-31"
            }
        ),
        TextNode(
            text="Louisa Coffee 路易莎【暖心蕎麥系列】新品上市。活動期間：2025/11/20 起。新品價格：蕎麥茶 45 元、蕎麥鮮奶茶 65 元。特色：嚴選慢火焙炒蕎麥，帶出自然穀物與堅果香氣，口感溫潤；鮮奶茶則將蕎麥香氣融入順口鮮奶，無咖啡因新選擇。全台門市同步販售。",
            metadata={
                "store_name": "路易莎 Louisa Coffee",
                "category": "新品上市",
                "topic": "暖心蕎麥系列",
                "keywords": ["蕎麥茶", "蕎麥鮮奶茶", "45元", "65元", "無咖啡因", "熱飲"],
                "valid_start": "2025-11-20",
				"valid_end": "2025-12-31"
            }
        )
	 ]
    return nodes
