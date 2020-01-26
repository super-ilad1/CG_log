# from googletrana import Translator
# -*- coding: utf-8 -*-
import time
import random
import hashlib
import requests
import json

import sys
sys.path.append(r"D:\PycharmProject\CG_log_web\firstApp\test\model.py")
from model import *
a=doMysql()
# 翻译标题模型



def get_tra_res(q,fromLang='en',toLang='zh'):
        url = "http://api.fanyi.baidu.com/api/trans/vip/translate"

        appid = '20190820000327938'  # 你的appid
        secretKey = 'oc_eEwR2S07uiI9ewqOm'  # 你的密钥
        salt = random.randint(32768, 65536)

    # q是你的query,就是你需要翻译的文本
    #生成签名
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
    #post请求参数
        data = {
            "appid": appid,
            "q": q,
            "from": fromLang,
            "to" : toLang,
            "salt" : str(salt),
            "sign" : sign,
            "action":"1"
        }
    #post请求
        res = requests.post(url, data=data)
    #返回时一个json
        trans_result = json.loads(res.content).get('trans_result')[0].get("dst")
        # error_code = json.loads(res.content).get('trans_result')[0].get("error_code")
        return trans_result

infos=a.DoMysql('select ID,title from c4d_url limit 10')
# print(infos)
for item in infos:

    # print(item[0],item[1])
    result=get_tra_res(item[1])
    print("result:",result)
    ID=item[0]
    a.DoMysql('UPDATE c4d_url SET trans_title = (%s) WHERE ID =(%s)',(result,ID))
    time.sleep(3)






# for i in get_tra_res(p):
#     print(i.get(''))