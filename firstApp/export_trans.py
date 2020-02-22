import socket
import sys


import pandas as pd


if not "-" in  socket.gethostname():
    sys.path.append(r"/home/cg_log/CG_log/firstApp")

else:
    sys.path.append(r"D:\PycharmProject\CG_log_web\firstApp")
# 包的根目录

from my_mysql_ORM import *

a = doMysql()

switch=2

# export df
if switch==1:


    datas=pd.read_sql("select post_ID,title, trans_title FROM c4d_url where trans_title is not null", a.mydb)

    datas.to_csv(r"D:\PycharmProject\CG_log_web\firstApp\test\trans_compare.csv")

# import and update
else:
    df = pd.read_csv(r"D:\PycharmProject\CG_log_web\firstApp\test\trans_compare.csv", encoding='gbk')
    df=df.set_index("post_ID",drop=True)
    print(df.columns)

    for index in df.index:
        ID=index
        trans_title=df.loc[index,"trans_title"]

        trans_title="C4D:"+trans_title
        # print(ID,"------------",str(trans_title),"------------",)
        a.DoMysql("UPDATE c4d_url SET trans_title = (%s) where post_ID=(%s)",(trans_title,ID))
        print('_'*100)