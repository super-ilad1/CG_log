# from googletrana import Translator
# -*- coding: utf-8 -*-
import time
import random
import hashlib
import requests
import json
import re
import sys


# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json

from extract_from_divText import extracted_translate

et=extracted_translate()

def translate(text,from_lang='en',to_lang='zh'):
    appid = '20190820000327938'  # 填写你的appid
    secretKey = 'oc_eEwR2S07uiI9ewqOm'  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = from_lang   #原文语种
    toLang = to_lang   #译文语种
    salt = random.randint(32768, 65536)
    q= text
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign+"&action"+"1"+"&domain"+"electronics"

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        return result['trans_result']
        #result['trans_result']  的结果是[{'src': 'apple', 'dst': '苹果'}]
    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()

sys.path.append(r"D:\PycharmProject\CG_log_web\firstApp\test\model.py")
from model import *
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码
a = doMysql()


def filter(text):
    filter_dict=[('cinema 4d','C4D'),
                 ('Cinema 4d','C4D'),
                 ('Cinema 4D','C4D'),
                 ('After Effects','AE'),

                                                   ]
    for item in filter_dict:
        text=text.replace(item[0],item[1])
    return text


real_problem=[]
count=0
error_list=[]
for item in a.DoMysql("select ID,content FROM c4d_content where from_url in (select URL FROM c4d_url where title like '%?' and trans_title is not null) and ID >= 176 and trans_content is null"):
    count+=1
    print("Dealing with nth",count," content....ID: ",item[0])
    ID=item[0]
    text=filter(item[1])
    try:
        text_outcome=et.div_translate(text)
        a.DoMysql("update c4d_content SET trans_content =(%s) where ID=(%s)", (text_outcome, ID))

    except Exception as e:
        print("出现错误...",'错误在ID: ',ID,'错误原因:',e)
        error_list.append([ID,e])

    time.sleep(1)
    print('_'*100)


print('所有出现错误的ID:\n'," 原因: ".join([str(item) for item in error_list]))


