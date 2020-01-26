import sys
sys.path.append(r"D:\PycharmProject\CG_log_web\firstApp\test")
#包的根目录
import random
from model import doMysql
a=doMysql()
outcome = a.DoMysql(
    "select * from (select Unit,author_alias FROM c4d_url  inner join c4d_content on c4d_content.from_url=c4d_url.URL where c4d_url.trans_title is not null) as  b  ")
print('selected finished')
for item in range(10):
    
    print(item)
    print( [item for item in outcome if item[0]==896997])