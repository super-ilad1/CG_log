# coding=utf-8
import time
import http.client
import hashlib
import urllib
import random
import json
import re
import pandas
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

        return result['trans_result'][0]['dst']
        #result['trans_result']  的结果是[{'src': 'apple', 'dst': '苹果'}]
    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()

with open("term_json",'r',encoding='utf-8', errors='ignore') as f:
    json_data=json.loads(f.read())

# 让匹配单词按顺序排列，单词数量越多的，越在前面
json_data = pandas.DataFrame(json_data)
json_data['words_amount']=json_data['term'].map(lambda x:len(x.split(" ")))
json_data=json_data.sort_values('words_amount',ascending=False)



# 测试是否有匹配的单词
def if_match(matched_word,text):
    if_true=lambda matched_word,text:bool(re.search(r'\b{}\b'.format(matched_word), text))
    if if_true(matched_word,text):
        return 1
    elif if_true(matched_word.lower(),text):
        return 2
    else:
        return 3

def replace_term(wait_trans):
    global json_data
    record_list=[]
    for index, item in json_data.iterrows():
        # print(item['term'])

        if if_match(item['term'],wait_trans)==1:
            wait_trans=wait_trans.replace(item['term'],item['medium'])
            record_list.append(item.to_dict())
        elif if_match(item['term'],wait_trans)==2:
            wait_trans=wait_trans.replace(item['term'].lower(),item['medium'])
            record_list.append(item.to_dict())

    return record_list,wait_trans


if __name__ == '__main__':
    wait_trans = "Specular issues"
    print(translate(wait_trans))
    time.sleep(1)
    # print(json_data)
    # print(json_data)



    # json_data['words_amount']
    # 先转化成首字母大写
    # capitalize=" ".join([item.capitalize() for item in wait_trans.split(" ")])

    # replace like  0000
    # wait_trans=replace_term(wait_trans)
    # print(wait_trans)
    # wait_trans_text=wait_trans[-1]
    # wait_trans_dict=wait_trans[0:-1]
    # print(wait_trans_dict)
    #
    # wait_trans_text=translate(wait_trans_text)
    # print(wait_trans_text)
    # for item in wait_trans_dict[0]:
    #     replace_first=item['medium']
    #     replace_second=item['trans']
    #     print(replace_second)
    #     wait_trans_text=wait_trans_text.replace(replace_first,replace_second,1)
    #
    # print(wait_trans_text)