# -*- coding: utf-8 -*-

from predicate.predicate import W

p_when = (W("何时") | W("时候"))
p_where = (W("哪里") | W("哪儿") | W("何地") | W("何处") | W("在") + W("哪"))

p_higher = (W("大于") | W("高于"))
p_lower = (W("小于") | W("低于"))
p_compare = (p_higher | p_lower)

# TODO 先判断属性是否可以度量（1）刻度量且又标准属性，用标准属性（2）剩余的用score解决
# TODO or w.token in opinions[entity_attribute] **
p_better = (W("大") | W("小") | W("高") | W("低") | W("多") | W("少") | W("长") | W("短") |
            W("酸") | W("甜") | W("苦") | W("辣") | W("咸") | W("淡") |
            W("软") | W("硬") | W("松") | W("紧") | W("粗") | W("细") | W("厚") | W("薄") | W("深") | W("浅") |
            W("好"))

p_question = (W("好不好") | W("高不高") | W("快不快") | W("怎么样"))

higher = (W("大于") | W("高于"))
lower = (W("小于") | W("低于"))
compare = (higher | lower)

english_name = (W("英文名") | W("英文") + W("名字"))
introduction = (W("介绍") | W("是") + W("简介"))
rating = (W("评分") | W("分") | W("分数"))


