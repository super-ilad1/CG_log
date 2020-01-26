import sys
sys.path.append(r"D:\PycharmProject\CG_log_web\firstApp\test")
#包的根目录
import random
from model import doMysql
a=doMysql()
portrait=lambda number:f'/abc/portrait/image ({number}).jpg'
outcome=a.DoMysql("select * from (select Unit,author_alias FROM c4d_url  inner join c4d_content on c4d_content.from_url=c4d_url.URL where c4d_url.trans_title is not null) as  b  ")
print(len(outcome))
print(outcome)
name=set([item[1] for item in outcome])
print(name)
for item in name:
    print(item)
    portrait=f'/abc/portrait/image ({random.randint(1,1000)}).jpg'
    print(portrait)
    a.DoMysql("update c4d_content SET portrait =(%s) where author_alias=(%s)",(portrait,item))