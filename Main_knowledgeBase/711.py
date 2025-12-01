from llama_index.core.schema import TextNode
from typing import List


def get_kumamon_card_nodes() -> List[TextNode]::
   
	nodes = [

        # ------------------------------------------------------------
        #  一、超值組合
        # ------------------------------------------------------------

        TextNode(
            text="7-ELEVEN 超值組合【45元餐】。活動期間：2025/11/12 至 2025/12/09。指定麵包搭配指定飲料享 45 元優惠。主食包含：蛋黃奶香麵包、奶酥麵包、巧克力麵包等。飲料甜品任選：光泉無加糖濃豆漿、波蜜一日蔬果紫色蔬果汁、每日C 100%荔枝綜合果汁、波蜜低卡蔬果汁、德記洋行烏龍鮮綠茶、瑞穗巧克力牛奶、BODYTALK 高纖低脂牛乳。加 10 元可升級 CITY CAFE 中杯拿鐵（冰/熱）。",
            metadata={
                "store_name": "7-ELEVEN",
                "category": "超值組合",
                "topic": "45元餐",
                "keywords": ["45元", "早餐", "銅板價", "麵包", "飲料", "甜品", "省錢", "超值組合"],
                "valid_start": "2025-11-12",
                "valid_end": "2025-12-09"
            }
        ),

        TextNode(
            text="7-ELEVEN 超值組合【55元餐】。活動期間：2025/11/12 至 2025/12/09。指定丹麥吐司、起司麵包、巧克力麵包等搭配指定飲料可享 55 元優惠。飲料甜品任選：光泉無加糖濃豆漿、波蜜一日蔬果紫色蔬果汁、每日C 100%荔枝綜合果汁、波蜜低卡蔬果汁、德記洋行烏龍鮮綠茶、瑞穗巧克力牛奶、BODYTALK 高纖低脂牛乳。加 10 元可升級 CITY CAFE 中杯拿鐵（冰/熱）。",
            metadata={
                "store_name": "7-ELEVEN",
                "category": "超值組合",
                "topic": "55元餐",
                "keywords": ["55元", "早餐", "麵包", "飲料", "超值組合"],
                "valid_start": "2025-11-12",
                "valid_end": "2025-12-09"
            }
        ),

        TextNode(
            text="7-ELEVEN 超值組合【65元餐】。活動期間：2025/11/12 至 2025/12/09。指定豬肉起司蛋鬆餅堡、雞肉漢堡、牛肉堡等主餐搭配指定飲料享 65 元優惠。飲料甜品任選：光泉無加糖濃豆漿、波蜜一日蔬果紫色蔬果汁、每日C 100%荔枝綜合果汁、波蜜低卡蔬果汁、德記洋行烏龍鮮綠茶、瑞穗巧克力牛奶、BODYTALK 高纖低脂牛乳。加 10 元可升級 CITY CAFE 中杯拿鐵（冰/熱）。",
            metadata={
                "store_name": "7-ELEVEN",
                "category": "超值組合",
                "topic": "65元餐",
                "keywords": ["65元", "堡類", "飲料", "甜品", "超值組合"],
                "valid_start": "2025-11-12",
                "valid_end": "2025-12-09"
            }
        ),

        TextNode(
            text="7-ELEVEN 超值組合【75元餐】。活動期間：2025/11/12 至 2025/12/09。指定雞腿堡、雙層牛肉堡、豬肉起司堡等主餐搭配指定飲料享 75 元優惠。飲料甜品任選：光泉無加糖濃豆漿、波蜜一日蔬果紫色蔬果汁、每日C 100%荔枝綜合果汁、波蜜低卡蔬果汁、德記洋行烏龍鮮綠茶、瑞穗巧克力牛奶、BODYTALK 高纖低脂牛乳。加 10 元可升級 CITY CAFE 中杯拿鐵（冰/熱）。",
            metadata={
                "store_name": "7-ELEVEN",
                "category": "超值組合",
                "topic": "75元餐",
                "keywords": ["75元", "堡類", "飲料", "甜品", "超值組合"],
                "valid_start": "2025-11-12",
                "valid_end": "2025-12-09"
            }
        ),

        TextNode(
            text="7-ELEVEN 超值組合【85元餐】。活動期間：2025/11/12 至 2025/12/09。指定雞腿飯、豬排飯、牛肉飯等主餐搭配指定飲料可享 85 元優惠。飲料甜品任選：光泉無加糖濃豆漿、波蜜一日蔬果紫色蔬果汁、每日C 100%荔枝綜合果汁、波蜜低卡蔬果汁、德記洋行烏龍鮮綠茶、瑞穗巧克力牛奶、BODYTALK 高纖低脂牛乳。加 10 元可升級 CITY CAFE 中杯拿鐵（冰/熱）。",
            metadata={
                "store_name": "7-ELEVEN",
                "category": "超值組合",
                "topic": "85元餐",
                "keywords": ["85元", "飯類", "飲料", "甜品", "超值組合"],
                "valid_start": "2025-11-12",
                "valid_end": "2025-12-09"
            }
        ),

        TextNode(
            text="7-ELEVEN 超值組合【95元餐】。活動期間：2025/11/12 至 2025/12/09。指定豬肉起司蛋鬆餅堡、雞肉漢堡、牛肉堡等主餐搭配指定飲料可享 95 元優惠。飲料甜品任選：光泉無加糖濃豆漿、波蜜一日蔬果紫色蔬果汁、每日C 100%荔枝綜合果汁、波蜜低卡蔬果汁、德記洋行烏龍鮮綠茶、瑞穗巧克力牛奶、BODYTALK 高纖低脂牛乳。加 10 元可升級 CITY CAFE 中杯拿鐵（冰/熱）。",
            metadata={
                "store_name": "7-ELEVEN",
                "category": "超值組合",
                "topic": "95元餐",
                "keywords": ["95元", "堡類", "飲料", "甜品", "超值組合"],
                "valid_start": "2025-11-12",
                "valid_end": "2025-12-09"
            }
        ),

        # ------------------------------------------------------------
        # 二、蔬食優惠
        # ------------------------------------------------------------

        TextNode(
            text="7-ELEVEN 天素地蔬【米食類】優惠。活動期間 2025/10/06 至 2025/12/20。於農曆初一與十五購買指定冷藏或冷凍米食商品可享單件 95 折。品項包含：陽明春天古早味香菇竹筍粥、祥和川味水煮牛燴飯、松露菇菇燉飯、香鬆紫米風味飯糰、陽明春天野菇炊飯飯糰、塔香G丁燴飯、祥和塔香香鬆飯糰、松露蕈菇燕麥粥。",
            metadata={
                "store_name": "7-ELEVEN",
                "category": "蔬食優惠",
                "topic": "米食優惠",
                "keywords": ["素食", "米食", "初一十五", "95折", "天素地蔬", "飯糰", "燉飯", "健康"],
                "valid_start": "2025-10-06",
                "valid_end": "2025-12-20"
            }
        ),

        TextNode(
            text="7-ELEVEN 天素地蔬【麵食類】優惠。活動期間 2025/10/06 至 2025/12/20。於農曆初一與十五購買指定冷藏麵食可享單件 95 折。品項包含：日式豆皮蕎麥風味冷麵、金沙烤豆腐義大利麵、小小樹食繽紛時蔬青醬筆管麵、義式蕃茄蕈菇義大利麵。",
            metadata={
                "store_name": "7-ELEVEN",
                "category": "蔬食優惠",
                "topic": "麵食優惠",
                "keywords": ["素食", "麵食", "義大利麵", "蕎麥冷麵", "初一十五", "95折"],
                "valid_start": "2025-10-06",
                "valid_end": "2025-12-20"
            }
        ),

		# ------------------------------------------------------------
        # 三、CITY CAFE
        # ------------------------------------------------------------

TextNode(
    text="2025/11/12 至 2025/11/25 期間，CITY CAFE 濃萃美式與濃萃拿鐵（大杯、特大杯）享任選第二杯半價，折扣依最低售價商品計算。",
    metadata={
        "store_name": "7-ELEVEN",
        "category": "CITY CAFE",
        "topic": "飲品第二杯優惠",
        "keywords": ["咖啡", "第二杯半價", "CITY CAFE"],
        "valid_start": "2025-11-12",
        "valid_end": "2025-11-25"
    }
)
	TextNode(
    text="2025/11/12 至 2025/11/25 於 7-ELEVEN 購買 CITY PRIMA 中杯精品美式或精品拿鐵，可獲得 OPENPOINT 10 點（點數使用期限至 2025/12/31）。",
    metadata={
        "store_name": "7-ELEVEN",
        "category": "CITY PRIMA",
        "topic": "購買贈點",
        "keywords": ["精品咖啡", "CITY PRIMA", "OPENPOINT"],
        "valid_start": "2025-11-12",
        "valid_end": "2025-11-25"
    }
)
	TextNode(
    text="2025/11/12 至 2025/11/25，CITY TEA 純奶茶系列享雙杯 88 元優惠，活動涵蓋多款奶茶品項。",
    metadata={
        "store_name": "7-ELEVEN",
        "category": "CITY TEA",
        "topic": "雙杯優惠",
        "keywords": ["奶茶", "CITY TEA", "雙杯優惠"],
        "valid_start": "2025-11-12",
        "valid_end": "2025-11-25"
    }
)
	TextNode(
    text="2025/11/12 至 2025/11/25，CITY PEARL 珍珠系列全品項享任選兩杯 99 元優惠，適用於多款珍珠茶飲及奶茶。",
    metadata={
        "store_name": "7-ELEVEN",
        "category": "CITY PEARL",
        "topic": "雙杯優惠",
        "keywords": ["珍珠飲品", "CITY PEARL", "雙杯優惠"],
        "valid_start": "2025-11-12",
        "valid_end": "2025-11-25"
    }
)
        # ------------------------------------------------------------
        # 四、支付工具優惠
        # ------------------------------------------------------------

        TextNode(
            text="7-ELEVEN 支付優惠【OPEN 錢包】。活動期間 2025/10/01 至 2025/12/31。使用 OPEN 錢包行動隨時取完成線上支付並綁定指定銀行信用卡可享最高 12% OPENPOINT 回饋。",
            metadata={
                "store_name": "7-ELEVEN",
                "category": "支付優惠",
                "topic": "OPEN錢包信用卡",
                "keywords": ["OPEN錢包", "行動支付", "電子錢包", "信用卡", "12%", "回饋"],
                "valid_start": "2025-10-01",
                "valid_end": "2025-12-31"
            }
        ),
	
	TextNode(
  text="2025/10/01 至 2025/12/31，OPEN 錢包綁定中國信託信用卡，單筆滿 300 元享 10% OPENPOINT 回饋（11 月名額已額滿）。",
  metadata={
    "category": "OPEN錢包",
    "store_name": "7-ELEVEN",
    "topic": "中信卡回饋",
    "date_start": "2025/10/01",
    "date_end": "2025/12/31",
    "keywords": ["中國信託", "信用卡", "10%", "OPENPOINT"]
  }
)

	TextNode(
  text="2025/10/01 至 2025/12/31，OPEN 錢包綁定玉山信用卡，單筆滿 200 元享 10% OPENPOINT 回饋（11 月名額已額滿）。",
  metadata={
    "category": "OPEN錢包",
    "store_name": "7-ELEVEN",
    "topic": "玉山卡回饋",
    "date_start": "2025/10/01",
    "date_end": "2025/12/31",
    "keywords": ["玉山", "信用卡", "10%", "OPENPOINT"]
  }
)

	TextNode(
  text="2025/10/01 至 2025/12/31，OPEN 錢包綁定兆豐信用卡，單筆滿 200 元享 10% OPENPOINT 回饋（11 月名額已額滿）。",
  metadata={
    "category": "OPEN錢包",
    "store_name": "7-ELEVEN",
    "topic": "兆豐卡回饋",
    "date_start": "2025/10/01",
    "date_end": "2025/12/31",
    "keywords": ["兆豐", "信用卡", "10%", "OPENPOINT"]
  }
)

        TextNode(
            text="7-ELEVEN OPEN 錢包回饋。活動期間 2025/10/01 至 2025/12/31。綁定國泰信用卡，單筆消費滿 200 元可享 7% OPENPOINT 回饋（11 月名額已額滿）。",
            metadata={
                "store_name": "7-ELEVEN",
                "category": "支付優惠",
                "topic": "國泰卡回饋",
                "keywords": ["OPEN錢包", "國泰", "7%", "回饋", "名額已滿"],
                "valid_start": "2025-10-01",
                "valid_end": "2025-12-31"
            }
        ),
    ]

    return nodes
