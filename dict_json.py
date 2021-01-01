# -*- coding: UTF-8 -*-
import json

#dict -> json
def toJson(file_name,dict):
    with open(file_name+'.json', 'w', encoding='utf-8') as f:
        json.dump(dict, f, ensure_ascii=False, indent='\t')

#list -> dict
def toDict(list_key,list_value):
    todict = {}

    for cnt in range(0,len(list_value)) :
        for i in range(0,len(list_key)) :
            todict[cnt+1] = dict(zip(list_key, list_value[cnt]))

    return todict

