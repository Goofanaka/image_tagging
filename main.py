# -*- coding: UTF-8 -*-
import crawling
import kakao
import dict_json
import google_api
import fruit_dict
import glob
import os
import tagdata
import img_to_mongo
from datetime import datetime
from pprint import pprint
import time


if __name__ == '__main__':
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"} #크롤링 헤더
    KEY = 'd6274cee123c4ba08049ac5f9dbb0c5a' #카카오api_key
    images = sorted(glob.glob('C:\\coupang_crawler\\images\\*.jpg'), key=os.path.getctime) #이미지 path
    key_list = ['filename','title','date','kakao_tag','google_tag','fruit_dict']
    # key_list = ['filename','title','date','kakao_tag','fruit_dict']
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  'C:\coupang_crawler\\crawl_and_tag\\google_credential.json'# google api key
    
    # 1) 크롤링 폴더 생성
    # crawling.make_dir('images')    #(폴더명)

    # 2) 크롤링 셋팅
    test_list = crawling.crawling(1,'images',header)       #(페이지 수, 이미지 저장 폴더명, 헤더값)
    # print(len(test_list)


    #3) 카카오 api
    kakao_tag_list = kakao.kakao_tag(KEY, images)       #(api키, 이미지파일)
    print(len(kakao_tag_list))

    #4) 구글 api
    google_tag_list = google_api.localize_objects(images)  #(이미지파일)
    print(len(google_tag_list))
    
    #5) 과일 사전
    fruit_list = fruit_dict.fruit_check(test_list)  #(크롤링한 데이터의 타이틀)
    # print(len(fruit_list))


    #6) 크롤링list + 카카오list + 구글list + 과일사전list
    for i in range(0,len(test_list)) :
        test_list[i].append(kakao_tag_list[i])
        test_list[i].append(google_tag_list[i])
        test_list[i].append(fruit_list[i])
    # pprint(test_list)

    #7) dict 변환
    res = dict_json.toDict(key_list,test_list)      #(key값 리스트, value값 리스트)
    for k in res.keys():
        date_obj = datetime.strptime(res[k]['date'], '%Y_%m_%d')
        data = tagdata.Tagdata(
            name = res[k]['filename'],
            date = date_obj,
            title = res[k]['title'],
            kakao_tag = res[k]['kakao_tag'],
            google_tag = res[k]['google_tag'],
            title_tag = res[k]['fruit_dict']
        )
        data.save()
        
    
    # pprint(res)

    #8) 이미지 파일 저장
    for i in images:
        example = img_to_mongo.Image(name = i[26:] )
        with open(i, 'rb') as img:
            name = i[26:]
            example.image.replace(img, filename = name)
            example.save()
            
    

    #9) json 변환
    # dict_json.toJson('test',res)        #(json파일명, dict)
