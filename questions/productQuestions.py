# -*- coding: utf-8 -*-

from template.prefix import SPARQL_PREXIX
from template.sparql import SPARQL_SELECT_TEM, SPARQL_COUNT_TEM, SPARQL_ASK_TEM, ORDER_ASC_TEM, ORDER_DESC_TEM, LIMIT_TEM
from predicate import *
import wordTagging
from questions.auxiliaryQuestions import AuxiliaryQuestionSet


class ProductQuestionSet:
    def __init__(self):
        pass

    @staticmethod
    def has_high_performance_question(word_objects):
        """
        问题一：询问某项属性竞争力高的产品有哪些
        :param word_objects:
        :return:
        """
        select = u"?brand ?model"

        cidname = None
        for w in word_objects:
            if w.pos == pos_cidname:
                cidname = w.token
                break

        if cidname is None:
            return None, 0

        sparql = None
        suffix = ORDER_DESC_TEM.format(key="?score") + LIMIT_TEM.format(limit=10)
        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?cid :catalogid_cidname '{cidname}'." \
                    u"?modelid :model_to_catalog ?cid." \
                    u"?modelid :model_brand ?brand." \
                    u"?modelid :model_model ?model." \
                    u"?modelid :model_to_function ?attrid." \
                    u"?attrid :function_name '{attr}'." \
                    u"?record :model_to_function_id ?modelid." \
                    u"?record :model_to_function_funcid ?attrid." \
                    u"?record :model_to_function_score ?score." .format(cidname=cidname,
                                                                         attr=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e,
                                                  suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def catalog_has_performance_question(word_objects):
        """
        问题二：询问有某项功能的品类有哪些
        :param
        word_objects:
        :return:
        """
        select = "?cidname"

        sparql = None
        suffix = ""
        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?cid :catalogid_cidname ?cidname." \
                    u"?modelid :model_to_catalog ?cid." \
                    u"?modelid :model_to_function ?attrid." \
                    u"?attrid :function_name '{attr}'.".format(attr=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e,
                                                  suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def ask_product_has_performance(word_objects):
        """
        问题三：询问某个产品是否具有某项功能
        :param
        word_objects:
        :return:
        """
        select = "?cidname"

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

        if not model:
            return None, 0
        else:
            if brand:
                brand = wordTagging.after_process(brand)
            model = wordTagging.after_process(model)

        sparql = None
        for w in word_objects:
            if w.pos == pos_attribute:
                if not brand:
                    e = u"?modelid :model_model '{model}'." \
                        u"?modelid :model_to_function ?attrid." \
                        u"?attrid :function_name '{attr}'.".format(model=model,
                                                                   attr=w.token)
                else:
                    e = u"?modelid :model_brand '{brand}'." \
                        u"?modelid :model_model '{model}'." \
                        u"?modelid :model_to_function ?attrid." \
                        u"?attrid :function_name '{attr}'.".format(brand=brand,
                                                                   model=model,
                                                                   attr=w.token)

                sparql = SPARQL_ASK_TEM.format(prefix=SPARQL_PREXIX,
                                               expression=e)
                break
        return sparql, len(select.split())

    @staticmethod
    def has_attribute_question(word_objects):
        """
        # 问题四：询问具某品类中有某项功能的产品有哪些
        :param word_objects:
        :return:
        """
        select = u"?brand ?model"

        cidname = None
        for w in word_objects:
            if w.pos == pos_cidname:
                cidname = w.token
                break

        if cidname is None:
            return None, 0

        sparql = None
        suffix = ORDER_DESC_TEM.format(key="?score")
        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?cid :catalogid_cidname '{cidname}'." \
                    u"?modelid :model_to_catalog ?cid." \
                    u"?modelid :model_brand ?brand." \
                    u"?modelid :model_model ?model." \
                    u"?modelid :model_to_function ?attrid." \
                    u"?attrid :function_name '{attr}'." \
                    u"?record :model_to_function_score ?score." \
                    u"?record :model_to_function_id ?modelid." \
                    u"?record :model_to_function_funcid ?attrid.".format(cidname=cidname,
                                                                         attr=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e,
                                                  suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def product_whether_nice_question(word_objects):
        """
        问题五：询问某品类中某个产品的某项属性好不好
        :param word_objects:
        :return:
        """
        select = "?score ?highest ?rank ?total"

        sparql = None
        suffix = ""

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

        e = "{" + AuxiliaryQuestionSet.product_has_performance_score_question(word_objects)[0][296:] + "}" + \
            "{" + AuxiliaryQuestionSet.product_highest_performance_question(word_objects)[0][296:].replace(
            "?brand ?model ", "") + "}" + \
            "{" + AuxiliaryQuestionSet.product_has_performance_rank_question(word_objects)[0][296:] + "}" + \
            "{" + AuxiliaryQuestionSet.product_has_performance_total_question(word_objects)[0][296:] + "}"

        sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                          select=select,
                                          expression=e,
                                          suffix=suffix)
        return sparql, len(select.split())

    @staticmethod
    def brand_has_count_of_product_question(word_objects):
        """
        问题六：某个品牌有多少某品类的产品
        :param word_objects:
        :return:
        """
        select = u"?modelid"

        sparql = None
        res = "?total"
        for w in word_objects:
            if w.pos == pos_cidname:
                e = u"?cid :catalogid_cidname '{cidname}'." \
                    u"?modelid :model_to_catalog ?cid.".format(cidname=w.token)

                sparql = SPARQL_COUNT_TEM.format(prefix=SPARQL_PREXIX,
                                                 select=select,
                                                 res=res,
                                                 expression=e)
                break
        return sparql, len(select.split())

    @staticmethod
    def care_product_aspect_question(word_objects):
        """
        问题七：在某个品类中用户一般关心什么属性/功能
        :param word_objects:
        :return:
        """
        select = u"?attr"

        sparql = None
        suffix = ""
        for w in word_objects:
            if w.pos == pos_cidname:
                e = u"?cid :catalogid_cidname '{cidname}'." \
                    u"?modelid :model_to_catalog ?cid." \
                    u"?modelid :model_to_function ?attrid." \
                    u"?attrid :function_name ?attr.".format(cidname=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e,
                                                  suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def top_biz_with_attr_question(word_objects):
        """
        问题八：列举某项指标排名前几的某品类产品
        :param word_objects:
        :return:
        """
        select = u"?brand ?model"

        cidname = None
        for w in word_objects:
            if w.pos == pos_cidname:
                cidname = w.token
                break

        if cidname is None:
            return None, 0

        sparql = None
        suffix = ORDER_DESC_TEM.format(key="?biz30day") + LIMIT_TEM.format(limit=5)
        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?cid :catalogid_cidname '{cidname}'." \
                    u"?modelid :model_to_catalog ?cid." \
                    u"?modelid :model_brand ?brand." \
                    u"?modelid :model_model ?model." \
                    u"?modelid :model_model ?biz30day." \
                    u"?modelid :model_to_function ?attrid." \
                    u"?attrid :function_name '{attr}'.".format(cidname=cidname,
                                                               attr=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e,
                                                  suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def has_color_question(word_objects):
        """
        问题九：某产品某属性具体值是什么
        :param word_objects:
        :return:
        """
        select = u"?attr"

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

        if not model:
            return None, 0
        else:
            if brand:
                brand = wordTagging.after_process(brand)
            model = wordTagging.after_process(model)

        sparql = None
        suffix= ""
        if not brand:
            e = u"?modelid :model_model '{model}'." \
                u"?modelid :hasColor ?attrid." \
                u"?attrid :function_name ?attr".format(model=model)
        else:
            e = "?modelid :model_brand '{brand}'." \
                u"?modelid :model_model '{model}'." \
                u"?modelid :hasColor ?attrid."\
                u"?attrid :function_name ?attr".format(brand=brand,
                                                       model=model)

        sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                          select=select,
                                          expression=e,
                                          suffix=suffix)
        return sparql, len(select.split())

    @staticmethod
    def show_detail_question(word_objects):
        """
        问题十：某产品某属性具体值是什么
        :param word_objects:
        :return:
        """
        select = u"?cid ?brand ?model"

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

        if not model:
            return None, 0
        else:
            if brand:
                brand = wordTagging.after_process(brand)
            model = wordTagging.after_process(model)

        sparql = None
        suffix = ""
        if not brand:
            e = u"?cidid :catalogid_cid ?cid." \
                u"?modelid :model_to_catalog ?cidid." \
                u"?modelid :model_brand ?brand." \
                u"?modelid :model_model '{model}'."\
                u"?modelid :model_model ?model.".format(model=model)
        else:
            e = u"?cidid :catalogid_cid ?cid." \
                u"?modelid :model_to_catalog ?cidid." \
                u"?modelid :model_brand '{brand}'." \
                u"?modelid :model_brand ?brand." \
                u"?modelid :model_model '{model}'." \
                u"?modelid :model_model ?model.".format(brand=brand,
                                                        model=model)

        sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                          select=select,
                                          expression=e,
                                          suffix=suffix)
        return sparql, len(select.split())
