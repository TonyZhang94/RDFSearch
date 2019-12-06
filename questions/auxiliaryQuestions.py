# -*- coding: utf-8 -*-

from template.prefix import SPARQL_PREXIX
from template.sparql import SPARQL_SELECT_TEM, SPARQL_COUNT_TEM, SPARQL_ASK_TEM, ORDER_ASC_TEM, ORDER_DESC_TEM, LIMIT_TEM
from predicate import *
import wordTagging


class AuxiliaryQuestionSet(object):
    def __init__(self):
        pass

    @staticmethod
    def product_has_performance_score_question(word_objects):
        """
        某品牌-型号某项属性的得分
        :param word_objects:
        :return:
        """
        select = u"?brand ?model ?attr ?score"

        brand = None
        for w in word_objects:
            if w.pos == pos_brand:
                brand = w.token
                break

        model = None
        for w in word_objects:
            if w.pos == pos_model:
                model = w.token
                break

        if not brand or not model:
            return None, 0
        else:
            brand = wordTagging.after_process(brand)
            model = wordTagging.after_process(model)

        sparql = None
        suffix = ""
        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?s :model_to_function ?o." \
                    u"?s :model_brand '{brand}'." \
                    u"?s :model_brand ?brand." \
                    u"?s :model_model '{model}'." \
                    u"?s :model_model ?model." \
                    u"?o :function_name '{function}'." \
                    u"?o :function_name ?attr." \
                    u"?x :model_to_function_id ?s." \
                    u"?x :model_to_function_funcid ?o." \
                    u"?x :model_to_function_score ?score.".format(function=w.token,
                                                                  brand=brand,
                                                                  model=model)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e,
                                                  suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def product_highest_performance_question(word_objects):
        """
        某品类某属性的最高得分
        :param word_objects:
        :return:
        """
        select = u"?brand ?model ?attr ?highest"

        cidname = None
        for w in word_objects:
            if w.pos == pos_cidname:
                cidname = w.token
                break

        if not cidname:
            return None, 0

        sparql = None
        suffix = ORDER_DESC_TEM.format(key="?highest") + LIMIT_TEM.format(limit=1)
        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?cid :catalogid_cidname '{cidname}'." \
                    u"?s :model_to_catalog ?cid." \
                    u"?s :model_to_function ?o." \
                    u"?s :model_brand ?brand." \
                    u"?s :model_model ?model." \
                    u"?o :function_name '{function}'." \
                    u"?o :function_name ?attr." \
                    u"?x :model_to_function_score ?highest." \
                    u"?x :model_to_function_id ?s." \
                    u"?x :model_to_function_funcid ?o.".format(cidname=cidname,
                                                               function=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e,
                                                  suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def product_has_performance_rank_question(word_objects):
        """
        指定brand，model的产品某项属性的排名
        :param
        word_objects:
        :return:
        """
        select = u"?other_score"

        brand = None
        for w in word_objects:
            if w.pos == pos_brand:
                brand = w.token
                break

        model = None
        for w in word_objects:
            if w.pos == pos_model:
                model = w.token
                break

        if not brand or not model:
            return None, 0
        else:
            brand = wordTagging.after_process(brand)
            model = wordTagging.after_process(model)

        sparql = None
        rank = "?rank"
        suffix = ""
        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?s :model_to_function ?o." \
                    u"?s :model_brand ?brand." \
                    u"?s :model_model ?model." \
                    u"?o :function_name '{function}'." \
                    u"?o :function_name ?attr." \
                    u"?x :model_to_function_score ?other_score." \
                    u"?x :model_to_function_id ?s." \
                    u"?x :model_to_function_funcid ?o.".format(function=w.token) + \
                    u"{" \
                    u"  SELECT DISTINCT ?cid ?score WHERE {" + \
                    u"    ?s :model_to_catalog ?cid." \
                    u"    ?s :model_to_function ?o." \
                    u"    ?s :model_to_function ?o." \
                    u"    ?s :model_to_function ?o." \
                    u"    ?o :function_name '{function}'." \
                    u"    ?s :model_brand '{brand}'." \
                    u"    ?s :model_model '{model}'." \
                    u"    ?x :model_to_function_score ?score." \
                    u"    ?x :model_to_function_id ?s." \
                    u"    ?x :model_to_function_funcid ?o.".format(function=w.token,
                                                                   brand=brand,
                                                                   model=model) + \
                    u"  }" \
                    u"}" \
                    u"Filter(?other_score >= ?score)." \
                    u"?s :model_to_catalog ?cid."

                sparql = SPARQL_COUNT_TEM.format(prefix=SPARQL_PREXIX,
                                                 select=select,
                                                 res=rank,
                                                 expression=e,
                                                 suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def product_has_performance_total_question(word_objects):
        """
        品类拥有某项属性的产品有多少个
        :param
        word_objects:
        :return:
        """
        select = u"?s"

        cidname = None
        for w in word_objects:
            if w.pos == pos_cidname:
                cidname = w.token
                break

        if not cidname:
            return None, 0

        sparql = None
        res = "?total"
        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?cid :catalogid_cidname '{cidname}'." \
                    u"?s :model_to_catalog ?cid." \
                    u"?s :model_to_function ?o." \
                    u"?o :function_name '{function}'.".format(cidname=cidname,
                                                              function=w.token)

                sparql = SPARQL_COUNT_TEM.format(prefix=SPARQL_PREXIX,
                                                 select=select,
                                                 res=res,
                                                 expression=e)
                break
        return sparql, len(select.split())
