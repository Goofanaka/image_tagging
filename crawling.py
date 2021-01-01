# -*- coding: UTF-8 -*-
import errno
from urllib.request import urlretrieve
import re
import os
from bs4 import BeautifulSoup
import requests
from datetime import datetime

#폴더 만들기
def make_dir(folder_name):
    try:
        if not (os.path.isdir(folder_name)):
            os.makedirs(os.path.join(folder_name))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("오류ㅡㅡ")
            exit()

# 크롤링 함수
def crawling(page,folder_name,headers):

    craw_list = []
    str_date = datetime.now().strftime('%Y_%m_%d')
    cnt = 1

    for page in range(1, page+1):
        # 페이지 설정
        url = 'https://www.coupang.com/np/categories/194282?listSize=120&page={}'.format(page)
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        # 이미지 태그 리스트 불러오기
        data1_list = soup.find_all('dt', attrs={'class': 'image'})

        for li in data1_list:
            img = li.find("img")  # img 태그 찾기
            title = img["alt"]  # 제목 alt 넣은거
            img_src = 'http:' + img["src"]  # img 다운 url완성
            title = re.sub("[^0-9a-zA-Zㄱ-힗]", "", title)  # title 특수문자,공백 제거
            savename = str_date + '_' + str(cnt) + '.jpg'
            urlretrieve(img_src, './' + folder_name + '/' + savename)  # 이미지 크롤링(제목 : 날짜)

            craw_list.append([savename, title, str_date])      #list 저장
            cnt += 1

    return craw_list


