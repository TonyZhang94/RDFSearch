# -*- coding: utf-8  -*-

import os
import pandas as pd


def answer_select(values, selects, mode="SIGROW"):
    if len(values) == 0:
        print('I don\'t know. :(')
    else:
        for inx in range(0, len(values), selects):
            for i in range(selects):
                print(values[inx + i], end=" ")
            if "MULTROW" == mode:
                print()
            else:
                print("；", end="")
    print()


def answer_ask(value):
    if isinstance(value, bool):
        if value is True:
            print('Yes')
        else:
            print('I don\'t know. :(')
    else:
        print("Wrong answer type. :(")


def answer_whether_nice(value):
    if len(value) == 0:
        print('I don\'t know. :(')
    else:
        score, highest, rank, total = value
        percent = int(rank) / int(total)
        if percent <= 0.1:
            print("上等", end=" ")
        elif 0.1 < percent <= 0.25:
            print("中上", end=" ")
        elif 0.25 < percent <= 0.75:
            print("中等", end=" ")
        elif 0.75 < percent <= 0.9:
            print("中下", end=" ")
        else:
            print("下等", end=" ")
        print(f"{rank}/{total}")


def answer_count(values):
    if len(values) == 0:
        print('0个')
    else:
        print(f"{values[0]}个")


def answer_detail(values):
    if len(values) == 0:
        print('I don\'t know. :(')
    else:
        cid, brand, model = values
        print(cid, brand, model)
        for pcid in range(101):
            file = f"D:\KG for movie\kg_demo_movie\ProductQuery\data\data_pcid{pcid}cid{cid}.csv"
            if not os.path.exists(file):
                continue

            df = pd.read_csv(file, encoding="utf_8_sig", index_col=0)
            df = df[df["model"] == model]
            df = df[df["brand"] == brand]
            df = df.sort_values(["datamonth"], ascending=False)

            if len(df) == 0:
                print('I don\'t know. :(')

            cols = df.columns
            vals = df.values[0]
            for col, val in zip(cols, vals):
                try:
                    if len(val) > 20:
                        val = val[:20]
                        print(f"{col}: {val};", end="")
                        print('\033[1;30m%s\033[0m'%"……", end=" ")
                    else:
                        print(f"{col}: {val};", end=" ")
                except TypeError:
                    print(f"{col}: {val};", end=" ")
            print('\033[1;31m%s\033[0m'%" << 详情连接")
            break
