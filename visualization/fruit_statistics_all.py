import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import tagdata
import img_to_mongo
import collections
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def fruit_statistics_all():
    fruit_list = []
    tagdata_all = tagdata.Tagdata.objects()
    for i in tagdata_all:
        fruit_list.append(i.title_tag[0])
    fruit_dict = collections.Counter(fruit_list)  # 특정값들을 카운트해서 딕셔너리로 변경
    df = pd.DataFrame({'fruit': fruit_dict.keys(), 'count': fruit_dict.values()}).sort_values(by='count',ascending=False).reset_index(drop=True)
    color = sns.color_palette('hls', len(fruit_dict))
    plt.figure(figsize=(30, 10))
    plt.rc('font', family='Malgun Gothic')
    plt.title("쿠팡 랭킹 과일 수량 ", fontsize=18)
    plt.ylabel("과일 수량", fontsize=12)
    plt.xlabel("과일", fontsize=12)
    plt.yticks(fontsize=12)
    plt.xticks(rotation=60)
    plt.bar(df['fruit'], df['count'], align='center', color=color)
    for i, v in enumerate(df['fruit']):
        plt.text(v, df['count'][i], df['count'][i],
                 fontsize=10,
                 color='black',
                 horizontalalignment='center',
                 verticalalignment='bottom')
    plt.savefig('fruit_statistics_all.png', dpi=300)



fruit_statistics_all()
