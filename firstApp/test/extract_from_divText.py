import re

# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json
import time


class extracted_translate():

    def translate(self, text, from_lang='en', to_lang='zh'):
        appid = '20190820000327938'  # 填写你的appid
        secretKey = 'oc_eEwR2S07uiI9ewqOm'  # 填写你的密钥

        httpClient = None
        myurl = '/api/trans/vip/translate'

        fromLang = from_lang  # 原文语种
        toLang = to_lang  # 译文语种
        salt = random.randint(32768, 65536)
        q = text
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
            q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign + "&action" + "1" + "&domain" + "electronics"

        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)

            return result['trans_result'][0]['dst']
            # result['trans_result']  的结果是[{'src': 'apple', 'dst': '苹果'}]
        except Exception as e:
            print(e)
        finally:
            if httpClient:
                httpClient.close()

    def extract(self, text):
        return re.findall(r'(<[^<>]*>)|([^<>]+)', text)
        # return re.findall(r"<([A-Za-z][A-Za-z0-9]*)\\b[^>]*>(.*?)</\\1>",text)

    def final_filter(self, text):
        filter_dict = [('相机', '摄像机')]
        for item in filter_dict:
            text = text.replace(item[0], item[1])
        return text

    def div_translate(self, original_text):
        def return_real(object):
            if object[0]:
                return object[0]
            else:
                return object[1]


        first_state = [item for item in self.extract(original_text) if len(item[1]) > 1 or item[0]]
        print("first_state: ", first_state)
        first_state = [list(item) for item in first_state]
        count=0
        for item in first_state:
            if item[1]:
                count+=1
                print("正在翻译第",count,'个子句...:',item[1])

                item[1] = self.translate(item[1])
                time.sleep(1)
        print(first_state)
        second_state = "".join([return_real(item) for item in first_state])

        print("second_state: ", second_state)

        return second_state


if __name__ == '__main__':
    a = '''<div class="post_message">here's a tutorial that shows how <a href="https://www.thepixellab.net/c4d-tutorial-mograph-selection-deleting-individual-clones" rel="nofollow">https://www.thepixellab.net/c4d-tutorial-mograph-selection-deleting-individ...</a></div>'''
    et = extracted_translate()

    et.div_translate(a)
