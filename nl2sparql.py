# -*- coding: utf-8 -*-

import wordTagging
from rules.primary import rules


class NL2Sparql:
    def __init__(self):
        self.tw = wordTagging.Tagger()
        self.rules = rules

    def get_sparql(self, question):
        word_objects = self.tw.get_word_objects(question)
        # for obj in word_objects:
        #     print(obj.token, obj.pos)
        queries_dict = dict()

        for rule in self.rules:
            (query, selects), rule_id, condition_num = rule.apply(word_objects)

            if query is not None:
                queries_dict[condition_num] = (query, selects, rule_id)

        # print(queries_dict)
        if len(queries_dict) == 0:
            return None
        elif len(queries_dict) == 1:
            return list(queries_dict.values())[0]
        else:
            sorted_dict = sorted(queries_dict.items(), key=lambda item: item[0], reverse=True)
            return sorted_dict[0][1]
