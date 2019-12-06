# -*- coding: utf-8 -*-

from predicate.predicate import W


# TODO
pos_attribute = "nattr"
pos_brand = "nbr"
pos_cidname = "ncid"
pos_constant = "cons"
pos_model = "nmo"
pos_npcid = "npcid"

entity_attribute = (W(pos=pos_attribute))
entity_brand = (W(pos=pos_brand))
entity_cidname = (W(pos=pos_cidname))
entity_constant = (W(pos=pos_constant))
entity_model = (W(pos=pos_model))
entity_npcid = (W(pos=pos_npcid))


p_function = (W("功能") | W("作用"))
p_attribute = (W("属性") | W("功能") | W("作用") | W("方面"))
p_hasAbility = (W("可以") | W("能够"))
p_score = (W("得分") | W("分数"))
p_rank = (W("排名"))
p_total = (W("总共") | W("总数") | W("数量") | W("一共"))
p_highest = (W("最高得分") | W("最高分数") | W("最高分"))
p_cidname = (W("品类") | W("类别"))
p_care = (W("关心") | W("关注"))
p_example = (W("列举") | W("罗列"))
p_biz = (W("销售量") | W("销售数量"))
p_color = (W("颜色") | W("什么色"))
p_detail = (W("详细信息") | W("详细资料") | W("详情"))
