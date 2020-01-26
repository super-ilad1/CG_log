import re
record=''
from hanziconv import HanziConv
with open(r'D:\PycharmProject\CG_log_web\firstApp\test\original_term','r',encoding='utf-8') as f:
    content=f.readlines()
    for item in content:
        try:
            # print(item)
            item=item.replace("【","").replace("】","").replace("[","").replace("]","").replace("<","")

            chinese = re.findall(u"[\u4e00-\u9fa5]+",item)
            english = re.findall(u"[^(\u4e00-\u9fa5|\n)]+",item)
            if english[0][-1]==" ":
                english=english[0][:-1]
            else:
                english=english[0]
            if chinese[0]:
                chinese=chinese[0]
            chinese=HanziConv.toSimplified(chinese)
            # print(chinese)
            # print(english)
            # print('_'*100)
            record+=english+"|||"+chinese+"\n"
        except:
            pass
# print(record)
# with open('final_term.txt','w') as d:
#     d.write(record)


with open("final_term(1).txt",'w') as f:
    f.write(record)



