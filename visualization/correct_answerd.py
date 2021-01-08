import os
import sys
import tagdata
import img_to_mongo
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def correct_answerd():
    google_list = []
    kakao_list  = []

    tagdata_r = tagdata.Tagdata.objects()
    for i in tagdata_r:
        google_list.append([i.google_tag, i.title_tag])
        kakao_list.append([i.kakao_tag, i.title_tag])


    g_cnt = 0
    for i in range(len(google_list)):
        if google_list[i][1][0] in google_list[i][0]:
            g_cnt += 1
        elif google_list[i][1][0] == 'fruit_etc':
            g_cnt += 1

    k_cnt = 0
    for i in range(len(kakao_list)):
        if kakao_list[i][1][0] in kakao_list[i][0]:
            k_cnt += 1
        elif google_list[i][1][0] == 'fruit_etc':
            k_cnt += 1

    g_answer = round(g_cnt/len(google_list)*100,2)
    k_answer = round(k_cnt/len(google_list)*100,2)

    df = pd.DataFrame({"API":["google", "kakao"], "percent":[g_answer,k_answer]})

    plt.rc('font', family='Malgun Gothic')
    plt.title("google API, kakao API 성능 비교" ,fontsize = 18)
    plt.ylabel("정답률 (%)", fontsize=12)
    plt.ylim(0,100)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=12)
    plt.bar(df['API'], df['percent'],align='center', color=['royalblue','gold'])
    for i,v in enumerate(df['API']):
        plt.text(v, df['percent'][i], df['percent'][i],
                fontsize = 15, 
                color='black',
                horizontalalignment='center',
                verticalalignment='bottom')
    plt.savefig('correct_answerd.png', dpi=300, bbox_inches='tight')