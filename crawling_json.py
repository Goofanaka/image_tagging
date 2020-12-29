# -*- coding: UTF-8 -*-
import errno
from urllib.request import urlretrieve
import re
import os
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import cv2
import json
import glob
import base64

#폴더 만들기
try:
    if not (os.path.isdir('image')):
        os.makedirs(os.path.join('image'))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("오류ㅡㅡ")
        exit()

#접속 헤더값
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

#크롤링 함수
def crawling(soup):

    cnt = 1
    to_date = datetime.now()  # 현재시간
    str_date = to_date.strftime('%Y_%m_%d')  # str으로 타입 및 형식 변경


    #이미지 태그 리스트 불러오기
    data1_list = soup.find_all('dt', attrs={'class': 'image'})

    for li in data1_list:
        img = li.find("img")        #img 태그 찾기
        title = img["alt"]      #제목 alt 넣은거
        img_src = 'http:' + img["src"]      #img 다운 url완성
        title = re.sub("[^0-9a-zA-Zㄱ-힗]", "", title)        #title 특수문자,공백 제거
        savename = str_date + '_' + str(cnt) + '.jpg'

        urlretrieve(img_src, './image/' + savename)       # 이미지 크롤링(제목 : 날짜)
        # urlretrieve(img_src, './image/' + title + '.jpg')  # 이미지 크롤링(제목 : 과일타이틀)

        fruit_list.append([cnt, img_src, title, str_date])      #list 저장
        fruit_dict[savename] = {'img': img_src, 'title': title, 'date': str_date}       #dict 저장
        cnt += 1

    return fruit_list, fruit_dict

#json파일 만들기
def toJson(fruit_dict):
    with open('fruit.json', 'w', encoding='utf-8') as file:
        json.dump(fruit_dict, file, ensure_ascii=False, indent='\t')


if __name__ == '__main__':
    fruit_list = []
    fruit_dict = {}

    #페이지 설정
    for page in range(1, 2):
        res = requests.get('https://www.coupang.com/np/categories/194282?page={}'.format(page),headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        fruit_res = crawling(soup)     #크롤링하기
        fruit_list += fruit_res[0]      #list
        fruit_dict = dict(fruit_dict, **fruit_res[1])       #dict

    # #list 출력
    # for i in fruit_list:
    #     print(i)
    #
    # #dict 출력
    # for i in fruit_dict:
    #     print(i, fruit_dict[i]['img'], fruit_dict[i]['title'], fruit_dict[i]['date'])

    #image 폴더 파일 불러오기
    images = glob.glob('C:/Project2020/image/*.jpg')
    for img in images:
        # print(img)  #C:/Project2020/image\2020_12_29_7.jpg
        img_name = img.split('\\')[1]
        # print(img_name) #2020_12_30_9.jpg
        image = cv2.imread(img)
        data = cv2.imencode('.jpg', image)[1].tobytes()
        # print(data)
        # data2 = base64.b64encode(data)
        # data = data2.decode("UTF-8")   #str로 변경
        # fruit_dict[img_name] = {'img_bin': data}

    toJson(fruit_dict)      #dict를 json으로 만들기