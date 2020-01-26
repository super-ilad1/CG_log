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
    filter_dict=[('cinema 4d','C4D'),('Cinema 4d','C4D'),('Cinema 4D','C4D'),('After Effects','AE')]
    for item in filter_dict:
        text=text.replace(item[0],item[1])
    return text
real_problem=[]
count=0
for item in a.DoMysql("select ID,title from c4d_url where title like '%?'")[0:200]:
    count+=1

    real_problem.append(item)
    # 一个个的去请求会比较的慢，所以这里积累5个title就请求一次
    if (count%5)==0:
        ready_trans_content=[filter(i[1]) for i in real_problem]
        print(ready_trans_content)
        ready_trans_order=[i[0] for i in real_problem]
        query = "\n".join(ready_trans_content)
        trans_outcome_list=translate(query)
        trans_outcome_list=[item['dst'] for item in trans_outcome_list]
        print(trans_outcome_list)
        # print(real_problem[item])
        updated_list=[item for item in zip(ready_trans_order,trans_outcome_list)]
        print(updated_list)
        a.DoMysql("insert into c4d_url (ID,trans_title) values (%s,%s) ON DUPLICATE KEY UPDATE trans_title=VALUES(trans_title)",updated_list,Many=True)
        print('_'*100)

        real_problem=[]
        time.sleep(2)




