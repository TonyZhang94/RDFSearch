# -*- coding: utf-8 -*-

# TODO more
SPARQL_SELECT_TEM = u"{prefix}\n" + \
             u"SELECT DISTINCT {select} WHERE {{\n" + \
             u"{expression}\n" + \
             u"}}\n" + \
             u"{suffix}\n"

SPARQL_COUNT_TEM = u"{prefix}\n" + \
             u"SELECT (COUNT({select}) AS {res}) WHERE {{\n" + \
             u"{expression}\n" + \
             u"}}\n"

SPARQL_ASK_TEM = u"{prefix}\n" + \
             u"ASK {{\n" + \
             u"{expression}\n" + \
             u"}}\n"

ORDER_ASC_TEM = "ORDER BY {key}\n"

ORDER_DESC_TEM = "ORDER BY DESC({key})\n"

LIMIT_TEM = "LIMIT {limit}\n"

OFFSET_TMP = "OFFSET {offset}\n"
