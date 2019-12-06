# -*- coding: utf-8 -*-

from refo import Star, Any

from rules.rule import Rule
from predicate import *
from questions import *


DotStarNG = Star(Any(), greedy=False)
DotStar = Star(Any(), greedy=True)

rules = list()


# # 问题一：询问某项属性竞争力高的产品有哪些
rules.append(Rule(rule_id=1.1, condition_num=3, condition=entity_cidname + DotStarNG + entity_attribute + DotStarNG + p_better, action=ProductQuestionSet.has_high_performance_question))
rules.append(Rule(rule_id=1.2, condition_num=3, condition=entity_cidname + DotStarNG + p_better + DotStarNG + entity_attribute, action=ProductQuestionSet.has_high_performance_question))
rules.append(Rule(rule_id=1.3, condition_num=3, condition=entity_attribute + DotStarNG + p_better + DotStarNG + entity_cidname, action=ProductQuestionSet.has_high_performance_question))
rules.append(Rule(rule_id=1.4, condition_num=3, condition=p_better + DotStarNG + entity_attribute + DotStarNG + entity_cidname, action=ProductQuestionSet.has_high_performance_question))

# # 问题二：询问有某项功能的品类有哪些
rules.append(Rule(rule_id=2.1, condition_num=2, condition=p_cidname + DotStarNG + entity_attribute, action=ProductQuestionSet.catalog_has_performance_question))
rules.append(Rule(rule_id=2.2, condition_num=2, condition=entity_attribute + DotStarNG + p_cidname, action=ProductQuestionSet.catalog_has_performance_question))
rules.append(Rule(rule_id=2.3, condition_num=3, condition=p_hasAbility + DotStarNG + entity_attribute + DotStarNG + p_cidname, action=ProductQuestionSet.catalog_has_performance_question))

# # 问题三：询问某个产品是否具有某项功能
rules.append(Rule(rule_id=3.1, condition_num=4, condition=entity_brand + DotStarNG + entity_model + DotStarNG + p_hasAbility + DotStarNG + entity_attribute, action=ProductQuestionSet.ask_product_has_performance))
rules.append(Rule(rule_id=3.2, condition_num=4, condition=entity_model + DotStarNG + entity_brand + DotStarNG + p_hasAbility + DotStarNG + entity_attribute, action=ProductQuestionSet.ask_product_has_performance))
rules.append(Rule(rule_id=3.3, condition_num=3, condition=entity_model + DotStarNG + p_hasAbility + DotStarNG + entity_attribute, action=ProductQuestionSet.ask_product_has_performance))
rules.append(Rule(rule_id=3.4, condition_num=5, condition=entity_brand + DotStarNG + entity_model + DotStarNG + entity_cidname + DotStarNG + p_hasAbility + DotStarNG + entity_attribute, action=ProductQuestionSet.ask_product_has_performance))
rules.append(Rule(rule_id=3.5, condition_num=5, condition=entity_model + DotStarNG + entity_brand + DotStarNG + entity_cidname + DotStarNG + p_hasAbility + DotStarNG + entity_attribute, action=ProductQuestionSet.ask_product_has_performance))
rules.append(Rule(rule_id=3.6, condition_num=4, condition=entity_model + DotStarNG + entity_cidname + DotStarNG + p_hasAbility + DotStarNG + entity_attribute, action=ProductQuestionSet.ask_product_has_performance))
rules.append(Rule(rule_id=3.7, condition_num=3, condition=entity_brand + DotStarNG + entity_model + DotStarNG + entity_attribute, action=ProductQuestionSet.ask_product_has_performance))
rules.append(Rule(rule_id=3.8, condition_num=3, condition=entity_model + DotStarNG + entity_brand + DotStarNG + entity_attribute, action=ProductQuestionSet.ask_product_has_performance))
rules.append(Rule(rule_id=3.9, condition_num=2, condition=entity_model + DotStarNG + entity_attribute, action=ProductQuestionSet.ask_product_has_performance))
rules.append(Rule(rule_id=3.10, condition_num=4, condition=entity_brand + DotStarNG + entity_model + DotStarNG + entity_cidname + DotStarNG + entity_attribute, action=ProductQuestionSet.ask_product_has_performance))
rules.append(Rule(rule_id=3.11, condition_num=4, condition=entity_model + DotStarNG + entity_brand + DotStarNG + entity_cidname + DotStarNG + entity_attribute, action=ProductQuestionSet.ask_product_has_performance))
rules.append(Rule(rule_id=3.12, condition_num=3, condition=entity_model + DotStarNG + entity_cidname + DotStarNG + entity_attribute, action=ProductQuestionSet.ask_product_has_performance))

# # 问题四：询问具某品类中有某项功能的产品有哪些
rules.append(Rule(rule_id=4.1, condition_num=3, condition=entity_cidname + DotStarNG + p_hasAbility + DotStarNG + entity_attribute, action=ProductQuestionSet.has_attribute_question))
rules.append(Rule(rule_id=4.2, condition_num=3, condition=entity_cidname + DotStarNG + p_hasAbility + DotStarNG + entity_attribute, action=ProductQuestionSet.has_attribute_question))
rules.append(Rule(rule_id=4.3, condition_num=3, condition=p_hasAbility + DotStarNG + entity_attribute + DotStarNG + entity_cidname, action=ProductQuestionSet.has_attribute_question))

# # 问题五：询问某品类中某个产品的某项属性好不好
rules.append(Rule(rule_id=5.1, condition_num=4, condition=entity_brand + DotStarNG + entity_model + DotStarNG + entity_attribute + DotStarNG + p_question, action=ProductQuestionSet.product_whether_nice_question))
rules.append(Rule(rule_id=5.2, condition_num=4, condition=entity_model + DotStarNG + entity_brand + DotStarNG + entity_attribute + DotStarNG + p_question, action=ProductQuestionSet.product_whether_nice_question))
rules.append(Rule(rule_id=5.3, condition_num=3, condition=entity_model + DotStarNG + entity_attribute + DotStarNG + p_question, action=ProductQuestionSet.product_whether_nice_question))

# # 问题六：某个品牌有多少某品类的产品
rules.append(Rule(rule_id=6.1, condition_num=2, condition=entity_brand + DotStarNG + entity_cidname, action=ProductQuestionSet.brand_has_count_of_product_question))

# # 问题七：在某个品类中用户一般关心什么属性/功能
rules.append(Rule(rule_id=7.1, condition_num=3, condition=entity_cidname + DotStarNG + p_care + DotStarNG + p_attribute, action=ProductQuestionSet.care_product_aspect_question))
rules.append(Rule(rule_id=7.2, condition_num=3, condition=entity_cidname + DotStarNG + p_attribute + DotStarNG + p_care, action=ProductQuestionSet.care_product_aspect_question))
rules.append(Rule(rule_id=7.3, condition_num=3, condition=p_care + DotStarNG + entity_cidname + DotStarNG + p_attribute, action=ProductQuestionSet.care_product_aspect_question))

# # 问题八：列举某项指标排名前几的某品类产品
rules.append(Rule(rule_id=8.1, condition_num=3, condition=p_example + DotStarNG + p_biz + DotStarNG + entity_cidname, action=ProductQuestionSet.top_biz_with_attr_question))
rules.append(Rule(rule_id=8.2, condition_num=3, condition=entity_cidname + DotStarNG + p_biz + DotStarNG + p_example, action=ProductQuestionSet.top_biz_with_attr_question))

# # 问题九：某产品某属性具体值是什么
rules.append(Rule(rule_id=9.1, condition_num=3, condition=entity_brand + DotStarNG + entity_model + DotStarNG + p_color, action=ProductQuestionSet.has_color_question))
rules.append(Rule(rule_id=9.2, condition_num=3, condition=entity_model + DotStarNG + entity_brand + DotStarNG + p_color, action=ProductQuestionSet.has_color_question))
rules.append(Rule(rule_id=9.3, condition_num=2, condition=entity_model + DotStarNG + p_color, action=ProductQuestionSet.has_color_question))

# # 问题十：展示某个产品的具体属性
rules.append(Rule(rule_id=10.1, condition_num=3, condition=entity_brand + DotStarNG + entity_model + DotStarNG + p_detail, action=ProductQuestionSet.show_detail_question))
rules.append(Rule(rule_id=10.2, condition_num=3, condition=entity_model + DotStarNG + entity_brand + DotStarNG + p_detail, action=ProductQuestionSet.show_detail_question))
rules.append(Rule(rule_id=10.3, condition_num=2, condition=entity_model + DotStarNG + p_detail, action=ProductQuestionSet.show_detail_question))

# # 其他问题
# 某品牌-型号某项属性的得分
rules.append(Rule(rule_id=0.11, condition_num=4, condition=entity_brand + DotStarNG + entity_model + DotStarNG + DotStarNG + entity_attribute + DotStarNG + p_score, action=AuxiliaryQuestionSet.product_has_performance_score_question))
rules.append(Rule(rule_id=0.12, condition_num=4, condition=entity_model + DotStarNG + entity_brand + DotStarNG + DotStarNG + entity_attribute + DotStarNG + p_score, action=AuxiliaryQuestionSet.product_has_performance_score_question))
rules.append(Rule(rule_id=0.13, condition_num=4, condition=entity_model + DotStarNG + DotStarNG + entity_attribute + DotStarNG + p_score, action=AuxiliaryQuestionSet.product_has_performance_score_question))

# 某品类某属性的最高得分
rules.append(Rule(rule_id=0.21, condition_num=3, condition=entity_cidname + DotStarNG + entity_attribute + DotStarNG + p_highest, action=AuxiliaryQuestionSet.product_highest_performance_question))
rules.append(Rule(rule_id=0.22, condition_num=3, condition=entity_cidname + DotStarNG + p_highest + DotStarNG + entity_attribute, action=AuxiliaryQuestionSet.product_highest_performance_question))

# 指定brand，model的产品某项属性的排名
rules.append(Rule(rule_id=0.31, condition_num=4, condition=entity_brand + DotStarNG + entity_model + DotStarNG + DotStarNG + entity_attribute + DotStarNG + p_rank, action=AuxiliaryQuestionSet.product_has_performance_rank_question))
rules.append(Rule(rule_id=0.32, condition_num=4, condition=entity_model + DotStarNG + entity_brand + DotStarNG + DotStarNG + entity_attribute + DotStarNG + p_rank, action=AuxiliaryQuestionSet.product_has_performance_rank_question))
rules.append(Rule(rule_id=0.33, condition_num=4, condition=entity_model + DotStarNG + DotStarNG + entity_attribute + DotStarNG + p_rank, action=AuxiliaryQuestionSet.product_has_performance_rank_question))

# 某品类拥有某项属性的产品有多少个
rules.append(Rule(rule_id=0.41, condition_num=3, condition=entity_cidname + DotStarNG + entity_attribute + DotStarNG + p_total, action=AuxiliaryQuestionSet.product_has_performance_total_question))
rules.append(Rule(rule_id=0.42, condition_num=3, condition=entity_attribute + DotStarNG + entity_cidname + DotStarNG + p_total, action=AuxiliaryQuestionSet.product_has_performance_total_question))
