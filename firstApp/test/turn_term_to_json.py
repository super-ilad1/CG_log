# -*- coding: utf-8 -*-
import json

super_list=[]
with open("final_term(1).txt",'r',encoding='utf-8', errors='ignore') as f:
    unique_list=[]

    # 去重
    for i in f.readlines():
        unique_list.append(i)
    unique_list=set(unique_list)

    # 提取
    for i in unique_list:
        i=i.replace("\n","")
        i=i.split('|||')
        print(i)

        try:
            super_list.append({"term":i[0],"trans":i[1],"medium":"0"*len(i[1])})
        except:
            pass

print(super_list)
super_list=json.dumps(super_list, ensure_ascii=False)
print(super_list)
with open("term_json",'w',encoding='utf-8') as w:
    w.write(super_list)