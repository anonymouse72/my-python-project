import datetime

# 十天干和十二地支
TEN_GAN = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
TWELVE_ZHI = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

# 五虎遁（年干 -> 正月干）起始映射
FIVE_TIGER_MAP = {
    '甲': '丙', '己': '丙',
    '乙': '戊', '庚': '戊',
    '丙': '庚', '辛': '庚',
    '丁': '壬', '壬': '壬',
    '戊': '甲', '癸': '甲',
}

# 用于快速查找字符索引
GAN_INDEX_MAP = {g: i for i, g in enumerate(TEN_GAN)}
ZHI_INDEX_MAP = {z: i for i, z in enumerate(TWELVE_ZHI)}

# 节气日期（示例）
def get_solar_terms_for_year(year):
    """获取指定年份的节气时间（示例数据）。"""
    return [
        ("立春", datetime.datetime(year, 2, 4, 5, 0)),
        ("惊蛰", datetime.datetime(year, 3, 6, 6, 0)),
        ("清明", datetime.datetime(year, 4, 5, 9, 0)),
        ("立夏", datetime.datetime(year, 5, 5, 3, 0)),
        ("芒种", datetime.datetime(year, 6, 6, 8, 0)),
        ("小暑", datetime.datetime(year, 7, 7, 10, 0)),
        ("立秋", datetime.datetime(year, 8, 7, 9, 0)),
        ("白露", datetime.datetime(year, 9, 7, 1, 0)),
        ("寒露", datetime.datetime(year, 10, 8, 2, 0)),
        ("立冬", datetime.datetime(year, 11, 7, 9, 0)),
        ("大雪", datetime.datetime(year, 12, 7, 6, 0)),
        ("小寒", datetime.datetime(year + 1, 1, 5, 4, 0)),
    ]

def is_leap_year(year):
    """判断是否为闰年"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(year, month, day):
    """计算公历日期是该年的第几天"""
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29
    return sum(days_in_month[:month - 1]) + day

def calculate_year_pillar(year):
    """计算年柱"""
    gan_index = (year - 4) % 10
    zhi_index = (year - 4) % 12
    return TEN_GAN[gan_index], TWELVE_ZHI[zhi_index]

def get_month_pillar(birth_dt, year_gan):
    """计算月柱"""
    solar_terms = get_solar_terms_for_year(birth_dt.year)
    month_number = None

    for i in range(len(solar_terms) - 1):
        if solar_terms[i][1] <= birth_dt < solar_terms[i + 1][1]:
            month_number = i + 1
            break

    if month_number is None:
        month_number = 12

    month_zhi = TWELVE_ZHI[(2 + (month_number - 1)) % 12]
    first_month_gan = FIVE_TIGER_MAP[year_gan]
    first_gan_idx = GAN_INDEX_MAP[first_month_gan]
    month_gan_idx = (first_gan_idx + month_number - 1) % 10
    month_gan = TEN_GAN[month_gan_idx]

    return month_gan, month_zhi

def calculate_day_pillar(year, month, day):
    """计算日柱"""
    doy = day_of_year(year, month, day)
    last_two_digits = year % 100
    year_adjusted = last_two_digits - 1 if last_two_digits != 0 else 99

    total = 5 * year_adjusted + year_adjusted // 4 + doy
    if 1901 <= year <= 2000:
        total += 15

    seq = total % 60
    if seq == 0:
        seq = 60

    gan_index = (seq - 1) % 10
    zhi_index = (seq - 1) % 12

    return TEN_GAN[gan_index], TWELVE_ZHI[zhi_index]

def calculate_hour_pillar(day_gan_index, hour):
    """计算时柱"""
    hour_zhi_index = (hour + 1) // 2 % 12
    hour_gan_index = (day_gan_index * 2 + hour_zhi_index) % 10
    return TEN_GAN[hour_gan_index], TWELVE_ZHI[hour_zhi_index]

class AstrologyAnalyzer:
    def __init__(self, birth_date, gender):
        self.birth_date = birth_date
        # self.birth_time = birth_time
        self.gender = gender
        self.bazi = self._analyze_bazi()

    def _analyze_bazi(self):
        year, month, day,hour = self.birth_date
        # hour = self.birth_time
        print(year,month,day,hour)
        year_gan, year_zhi = calculate_year_pillar(year)
        month_gan, month_zhi = get_month_pillar(datetime.datetime(year, month, day, hour), year_gan)
        day_gan, day_zhi = calculate_day_pillar(year, month, day)
        hour_gan, hour_zhi = calculate_hour_pillar(TEN_GAN.index(day_gan), hour)

        return f"{year_gan}{year_zhi}{month_gan}{month_zhi}{day_gan}{day_zhi}{hour_gan}{hour_zhi}"


if __name__ == '__main__':
    birth_date = (1995, 10, 1, 12)
    # birth_time = 0
    gender = 'male'

    analyzer = AstrologyAnalyzer(birth_date, gender)
    print("八字排盘结果：",analyzer.bazi)
    # for key, value in analyzer.bazi.items():
    #     print(f"{key}: {value}")
