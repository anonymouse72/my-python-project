# -*- coding: utf-8 -*-
import json

from src.bean.Constant import Constant



#########################
#  工具函数
#########################
def parse_bazi(bazi_str:str):
    """
    输入形如 "乙亥 乙酉 乙丑 壬午"，返回[(干,支),(干,支),(干,支),(干,支)]
    """
    arr = bazi_str.strip().split()
    if len(arr)!=4:
        raise ValueError("需输入四柱(年柱 月柱 日柱 时柱)，示例：乙亥 乙酉 乙丑 壬午")
    ret=[]
    for p in arr:
        if len(p)!=2:
            raise ValueError(f"柱 '{p}' 格式应为2字(干+支)")
        gan,zhi = p[0],p[1]
        if gan not in Constant.TIANGAN_INFO:
            raise ValueError(f"未知天干: {gan}")
        if zhi not in Constant.DIZHI_INFO:
            raise ValueError(f"未知地支: {zhi}")
        ret.append((gan,zhi))
    return ret

def get_na_yin(gan,zhi):
    return Constant.NAYIN_DICT.get(gan+zhi,"")

def find_three_combos(z:str):
    """三合(申子辰 / 亥卯未 / 寅午戌 / 巳酉丑)"""
    if z in ["申","子","辰"]:
        return ("申","子","辰")
    elif z in ["亥","卯","未"]:
        return ("亥","卯","未")
    elif z in ["寅","午","戌"]:
        return ("寅","午","戌")
    elif z in ["巳","酉","丑"]:
        return ("巳","酉","丑")
    return ()

def get_ten_god_relationship(day_master_wx:str, other_wx:str):
    """日主五行 vs 其它干(五行)，十神(简化)"""
    if day_master_wx not in Constant.TEN_GOD_MAP:
        return ""
    return Constant.TEN_GOD_MAP[day_master_wx].get(other_wx,"")

def find_day_xun_kong(day_pillar_gz:str):
    """
    根据 "日柱" (如 "乙丑") 找到其所属旬, 返回 { 'kong': [...], 'xun_name':... }
    """
    for xun in Constant.XUN_TABLE_60:
        if day_pillar_gz in xun["list"]:
            return xun
    return None

def is_pillar_in_xunkong(pillar_z:str, day_xun_data:dict):
    """
    判断该 pillar 的地支是否在日柱所属旬的空亡列表中
    """
    if not day_xun_data:
        return False
    return (pillar_z in day_xun_data["kong"])


#########################
#  神煞(仅根据本柱地支，与年支/日支三合局对比) - 简化
#########################
def calc_shensha_for_one_pillar(zhi:str, year_zhi:str, day_zhi:str):
    """
    根据本柱地支，判断其是否驿马、桃花、华盖、将星(简单演示)。
    真实运用中往往结合年干/日干，或更多神煞规则。
    """
    res=[]
    # 驿马(看年支 or 日支 同组?), 这里演示常见：year_zhi, day_zhi => group => yima
    # 但一般说“驿马在四柱出现”才算。本处仅演示 => 若 'zhi' == yima_rule[ x ] => 叫"驿马"
    # 这里做简易处理: if zhi == (year_zhi/day_zhi 三合局对应) => '驿马'
    group_year = find_three_combos(year_zhi)
    group_day  = find_three_combos(day_zhi)

    if group_year in Constant.YIMA_RULE:
        if zhi == Constant.YIMA_RULE[group_year]:
            res.append("驿马(与年支同组)")
    if group_day in Constant.YIMA_RULE:
        if zhi == Constant.YIMA_RULE[group_day]:
            res.append("驿马(与日支同组)")

    # 桃花
    if group_year in Constant.TAOHUA_RULE:
        if zhi == Constant.TAOHUA_RULE[group_year]:
            res.append("桃花(与年支同组)")
    if group_day in Constant.TAOHUA_RULE:
        if zhi == Constant.TAOHUA_RULE[group_day]:
            res.append("桃花(与日支同组)")

    # 华盖
    if group_year in Constant.HUAGAI_RULE:
        if zhi == Constant.HUAGAI_RULE[group_year]:
            res.append("华盖(与年支同组)")
    if group_day in Constant.HUAGAI_RULE:
        if zhi == Constant.HUAGAI_RULE[group_day]:
            res.append("华盖(与日支同组)")

    # 将星
    if group_year in Constant.JIANGXING_RULE:
        if zhi == Constant.JIANGXING_RULE[group_year]:
            res.append("将星(与年支同组)")
    if group_day in Constant.JIANGXING_RULE:
        if zhi == Constant.JIANGXING_RULE[group_day]:
            res.append("将星(与日支同组)")

    return res


import json


class BaziCalculator:
    def __init__(self, bazi, constant):
        """
        初始化 BaziCalculator

        :param bazi: 八字字符串 (如 "乙亥 乙酉 乙丑 壬午")
        :param constant: 一个包含八字基础数据的常量类 (如天干五行、地支藏干、纳音、十神等)
        """
        self.bazi = bazi
        self.constant = constant  # 传入 Constant 配置对象

    #########################
    #  主函数: 输出每柱信息
    #########################
    def pillars_analysis_json(self) -> str:
        """
        解析八字并返回 JSON 格式的八字分析结果

        :return: JSON 字符串，包含天干、地支、纳音、星运、自坐、空亡、神煞等信息
        """
        # 1) 解析八字
        pillars = parse_bazi(self.bazi)  # 假设 parse_bazi 已经定义
        year_pillar, month_pillar, day_pillar, hour_pillar = pillars

        yg, yz = year_pillar
        mg, mz = month_pillar
        dg, dz = day_pillar
        hg, hz = hour_pillar

        # 2) 计算日主五行
        day_master_wx = self.constant.TIANGAN_INFO[dg]["wuxing"]

        # 3) 计算日柱所属旬（用于空亡分析）
        day_gz_full = dg + dz
        day_xun_data = find_day_xun_kong(day_gz_full)  # 假设 find_day_xun_kong 已经定义

        # 4) 结果字典
        output_dict = {}

        # 定义柱名
        name_map = ["年柱", "月柱", "日柱", "时柱"]
        four_pillars = [year_pillar, month_pillar, day_pillar, hour_pillar]

        # 年支、日支用于神煞分析
        year_zhi = yz
        day_zhi = dz

        # 5) 遍历每一柱进行分析
        for i, (gan, zhi) in enumerate(four_pillars):
            pillar_name = name_map[i]

            # (A) 天干、地支、纳音
            gz_str = gan + zhi
            na_yin = self.constant.NAYIN_DICT.get(gz_str, "")

            # (B) 计算十神 (日主 vs 当前天干)
            this_wx = self.constant.TIANGAN_INFO[gan]["wuxing"]
            star_name = get_ten_god_relationship(day_master_wx, this_wx)

            # (C) 计算自坐（地支藏干）
            canggan_arr = self.constant.DIZHI_INFO[zhi]["canggan"]

            # (D) 计算是否空亡
            in_kong = zhi in day_xun_data["kong"] if day_xun_data else False

            # (E) 计算神煞
            shensha_list = calc_shensha_for_one_pillar(zhi, year_zhi, day_zhi)

            # (F) 组装输出
            output_dict[pillar_name] = {
                "天干": gan,
                "地支": zhi,
                "纳音": na_yin,
                "主星": star_name,
                "自坐": canggan_arr,
                "空亡": "是" if in_kong else "否",
                "神煞": shensha_list if shensha_list else []
            }

        # 转换为 JSON 并返回
        return json.dumps(output_dict, ensure_ascii=False, indent=2)


#########################
#  演示调用 (无演示输出)
#########################
if __name__=="__main__":
    # 假设输入四柱: "乙亥 乙酉 乙丑 壬午"
    bazi_string = "乙亥 乙酉 乙丑 壬午"
    bazi_calculator = BaziCalculator(bazi_string, Constant)
    result_json = bazi_calculator.pillars_analysis_json()
    print(result_json)
