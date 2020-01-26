import re
import sys
sys.path.append(r"D:\PycharmProject\CG_log_web\firstApp\test")
#包的根目录
import random
from model import doMysql
a=doMysql()
filter=lambda x:'/post/'+re.findall('https://forums.creativecow.net/thread/19/(\d+)',x)[0]
recommen_list = a.DoMysql("select URL,trans_title from c4d_url where trans_title is not null and trans_title like '%?'")
recommen_list=[{'url':filter(item[0]),'title':item[1]} for item in recommen_list]
random.shuffle(recommen_list)
print(recommen_list[0:10])