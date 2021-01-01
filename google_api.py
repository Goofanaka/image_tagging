from google.cloud import vision
import os, io 
import six
import my_setting
import glob


def localize_objects(images):
    # from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    google_list = []
    for path in images:
        with open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        objects = client.object_localization(
            image=image).localized_object_annotations

        tags = []

        for object_ in objects:
            
            if object_.score >= 0.60:  # 일치 퍼센트
                tags.append(object_.name.lower())
        google_list.append(list(set(tags)))

    return google_list