# Common Const
DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 10
DEFAULT_FAIL = -1

# Cache Time
CACHE_FIVE_SECONDS = 5
CACHE_FIVE_MINUTE = 5 * 60
CACHE_MINUTE = 60
CACHE_HALF_HOUR = 60 * 30
CACHE_HOUR = 60 * 60
CACHE_TWELVE_HOUR = 60 * 60 * 12
CACHE_DAY = 60 * 60 * 24
CACHE_WEEK = 60 * 60 * 24 * 7
CACHE_MONTH = 60 * 60 * 24 * 30

# Request Timeout
REQUESTS_TIMEOUT = 15

CACHE_USER_CAPTCHA_KEY = "monarch:user:captcha:image:{}"
CACHE_USER_TOKEN = "monarch:user:token:{}"
CACHE_ADMIN_USER_CAPTCHA = "monarch:admin_user:captcha:image{}"
CACHE_ADMIN_USER_TOKEN = "monarch:admin_user:token:{}"

VERIFICATION_WAY = ["email", "phone"]

GAN = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
ZHI = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
ZODIAC = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
NUM_CN = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
SOLAR_TERMS = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑",
               "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
MONTH_CN = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
DAY_CN = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四",
          "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八",
          "廿九", "三十", "卅一"]

DAY_GZ_STR = "{}{}年{}{}月{}{}日"
LUNAR_DAY_STR = "{}年{}{}月{}"

ARABIC_TO_CN_NUM_MAP = {
    "0": "〇", "1": "一", "2": "二", "3": "三", "4": "四",
    "5": "五", "6": "六", "7": "七", "8": "八", "9": "九"
}

STARTING_YEAR = 1984


DEFAULT_SERVICES = [
    {
        "name": "灵签",
        "key": "lot",
        "url": ""
    },
    {
        "name": "命理前定数",
        "key": "mlqds",
        "url": ""
    },
    {
        "name": "四柱预测",
        "key": "szyc",
        "url": ""
    }
]


class ServiceType:
    LOTS = "lot"
