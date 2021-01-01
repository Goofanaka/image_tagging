# -*- coding: UTF-8 -*-
import crawling
import kakao
import dict_json
import google_api
import fruit_dict
import glob
import os
import my_setting

if __name__ == '__main__':
    header = {"User-Agent": my_setting.USER_AGENT} #크롤링 헤더
    KEY = my_setting.KAKAO_API_KEY   #카카오api_key
    images = sorted(glob.glob('*.jpg'), key=os.path.getctime) #이미지 path
    key_list = ['filename','title','date','kakao_tag','google_tag','fruit_dict']
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = my_setting.GOOGLE_API_KEY  # google api key

    #1) 크롤링 폴더 생성
    crawling.make_dir('images')    #(폴더명)

    #2) 크롤링 셋팅
    test_list = crawling.crawling(1,'images',header)       #(페이지 수, 이미지 저장 폴더명, 헤더값)
    # print(test_list)

    #3) 카카오 api
    kakao_tag_list = kakao.kakao_tag(KEY, images)       #(api키, 이미지파일)
    # print(kakao_tag_list)

    #4) 구글 api
    google_tag_list = google_api.localize_objects(images)  #(이미지파일)
    # print(google_tag_list)
    
    #5) 과일 사전
    fruit_list = fruit_dict.fruit_check(test_list)  #(크롤링한 데이터의 타이틀)
    # print(fruit_list)

    #6) 크롤링list + 카카오list + 구글list + 과일사전list
    for i in range(0,len(test_list)) :
        test_list[i].append(kakao_tag_list[i])
        test_list[i].append(google_tag_list[i])
        test_list[i].append(fruit_list[i])
    # print(test_list)

    #7) dict 변환
    res = dict_json.toDict(key_list,test_list)      #(key값 리스트, value값 리스트)
    print(res)

    #8) json 변환
    dict_json.toJson('test',res)        #(json파일명, dict)
