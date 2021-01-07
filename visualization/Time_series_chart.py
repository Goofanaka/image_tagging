import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from datetime import datetime
import tagdata
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import collections

def Full_time_series_data():

    a_list = []
    data = tagdata.Tagdata.objects()
    for i in data:
        a_list.append([(i.date).strftime('%Y-%m-%d'), i.title_tag[0]])

    df = pd.DataFrame(a_list, columns=['date','fruit']).groupby(by=['date','fruit']).size().unstack(level =1)
    df = df.transpose()
    df1 = df.sort_values(['2021-01-04','2021-01-05','2021-01-06'], axis=0, ascending=False, inplace=False)
    df2=df1.head(15)
    df3 = df2.transpose()

    #Line chart
    plt.rc('font', family='Malgun Gothic')
    df3.plot()
    plt.title("날짜별 과일 수량" ,fontsize=18)
    plt.xlabel("날짜", fontsize=12,)
    plt.legend(title='fruit', loc='center left', bbox_to_anchor=(1.05, 0.5))
    plt.savefig('Full_time_series_data1.png', dpi=300)

    #bar chart
    # plt.rc('font', family='Malgun Gothic')
    # df3.plot(kind='barh', stacked=True)
    # plt.title("날짜별 과일 수량", fontsize=18)
    # plt.ylabel("날짜", fontsize=12)
    # plt.legend(title='fruit', loc='center left', bbox_to_anchor=(1, 0.5))
    # plt.savefig('Full_time_series_data2.png', dpi=300)

