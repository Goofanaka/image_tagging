# -*- coding: UTF-8 -*-
import crawling
import kakao
import dict_json
import glob
import os

if __name__ == '__main__':
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"} #크롤링 헤더
    KEY = '카카오api_key'   #카카오api_key
    images = sorted(glob.glob('C:/Project2020/image/*.jpg'), key=os.path.getctime) #이미지 path
    key_list = ['filename','title','date','kakao_tag']

    #1) 크롤링 폴더 생성
    crawling.make_dir('jua')    #(폴더명)

    #2) 크롤링 셋팅
    test_list = crawling.crawling(1,'jua',header)       #(페이지 수, 이미지 저장 폴더명, 헤더값)
    print(test_list)

    #3) 카카오 api
    kakao_tag_list = kakao.kakao_tag(KEY, images)       #(api키, 이미지파일)
    print(kakao_tag_list)

    #4) 크롤링list + 카카오list
    for i in range(0,len(test_list)) :
        test_list[i].append(kakao_tag_list[i])
    print(test_list)

    #5) dict 변환
    res = dict_json.toDict(key_list,test_list)      #(key값 리스트, value값 리스트)
    print(res)

    #6) json 변환
    dict_json.toJson('test',res)        #(json파일명, dict)
