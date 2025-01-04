NUMBER_ARABIC = "0123456789"

NUMBER_LOW = "零一二三四五六七八九"
NUMBER_UP = "零壹贰叁肆伍陆柒捌玖"
NUMBER_LOW_MAP = dict(zip(NUMBER_ARABIC, NUMBER_LOW))
NUMBER_UP_MAP = dict(zip(NUMBER_ARABIC, NUMBER_UP))

UNIT_LOW = {10: "十", 100: "百", 1000: "千", 10000: "万", 100000000: "亿"}

UNIT_ORDER_LOW = ",十,百,千,万,十,百,千,亿,十,百,千,万,十,百,千".split(",")
UNIT_ORDER_UP = ",拾,佰,仟,万,拾,佰,仟,亿,拾,佰,仟,万,拾,佰,仟".split(",")
