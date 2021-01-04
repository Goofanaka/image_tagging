from google.cloud import vision
import os, io 
import six
import glob
import time

def localize_objects(images):
    # from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    google_list = []
    cnt = 0
    for path in images:
        with open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        objects = client.object_localization(
            image=image).localized_object_annotations

        cnt += 1

        tags = []
        try:
            for object_ in objects:
                
                if object_.score >= 0.50:  # 일치 퍼센트
                    tags.append(object_.name.lower())
        except Exception as e:
            # print('error occured' * 10)  # 에러 확인용 프린트문
            tags.append("error")

        google_list.append(list(set(tags)))

    return google_list