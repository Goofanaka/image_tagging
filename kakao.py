# -*- coding: UTF-8 -*-
import sys
from os import listdir
from os.path import isfile, join
import requests
import cv2
import glob


#카카오 태그 리스트 반환
def kakao_tag(KEY,images):
    API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate'
    headers = {'Authorization': 'KakaoAK {}'.format(KEY)}
    kakao_list = []
    try :
        for img in images:
            image = cv2.imread(img)
            image2 = cv2.imencode('.jpg', image)[1].tobytes()

            data = {'image' : image2} #이미지 받고
            resp = requests.post(API_URL, headers=headers, files=data) #요청보냄
            resp.raise_for_status()
            result = resp.json()['result']  #{'label_kr': ['과일', '감'], 'label': ['fruit', 'persimmon']}
            kakao_list.append(result['label'])

    except Exception as e:
        print(str(e))
        sys.exit(0)

    return kakao_list








