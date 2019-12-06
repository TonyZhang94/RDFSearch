# -*- coding: utf-8 -*-

import os
import jieba
import jieba.posseg as pseg


class Word(object):
    def __init__(self, token, pos):
        self.token = token
        self.pos = pos


class Tagger:
    def __init__(self, path="vocab/"):
        # TODO vocab_name_pos.txt
        files = os.listdir(path)
        for file in files:
            if "vocab" in file:
                jieba.load_userdict(os.path.join(path, file))

        # TODO splits.txt
        with open(os.path.join(path, "vocab_model_nmo.txt"), mode="r", encoding="utf-8") as fp:
            for line in fp.readlines():
                parts = line.split(" ")
                token = "-".join(parts[:-1])
                jieba.suggest_freq(token, False)

        # TODO splits.txt
        with open(os.path.join(path, "splits.txt"), mode="r", encoding="utf-8") as fp:
            for line in fp.readlines():
                token1, token2 = line.split()
                jieba.suggest_freq((token1, token2), True)

        # TODO merge.txt
        with open(os.path.join(path, "merge.txt"), mode="r", encoding="utf-8") as fp:
            for line in fp.readlines():
                token = line.strip()
                jieba.suggest_freq(token, False)

    @staticmethod
    def get_word_objects(sentence):
        return [Word(word, tag) for word, tag in pseg.cut(sentence)]


def pre_process(text):
    text = text.replace("\\", "反斜杠").replace("/", "反斜杠")
    text = text.replace(" ", "空格符")
    text = text.replace("·", "黑点符")
    text = text.replace("-", "横杠符")
    return text


def after_process(text):
    if isinstance(text, str):
        text = text.replace("反斜杠", "/")
        text = text.replace("空格符", " ")
        text = text.replace("黑点符", "·")
        text = text.replace("横杠符", "-")
    return text
