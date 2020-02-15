import sys
from django.template import loader
import re
import os


import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoTest5.settings')
django.setup()


from django.core.paginator import Paginator

from djangoTest5 import settings
# settings.configure()


sys.path.append(r"D:\PycharmProject\CG_log_web\firstApp")
# 包的根目录
from my_mysql_ORM import *

mysql = doMysql()

filter = lambda x: '/post/' + re.findall('https://forums.creativecow.net/thread/19/(\d+)', x)[0]
recommen_list = mysql.DoMysql(
    "select URL,trans_title from c4d_url where trans_title is not null and trans_title like '%?'")
recommen_list = [{'url': filter(item[0]), 'title': item[1]} for item in recommen_list]
recommen_list = recommen_list

# 分页paginator making,recommen_list是一个[{}]样式的列表
# 10意味着一个页面有10个数据单位显示
paginator = Paginator(recommen_list, 10)
# page是页面数，page_span意味着当你你的分页导航的隔壁页数显示，你不可能只有下一页和上一页
page = 1
page_span = [page - 2, page - 1, page, page + 1, page + 2]
try:

    page = paginator.page(page)
except:
    pass

context = {'data': page, 'page_span': page_span}

    # s使用模板
    # 1. 加载模板文件，返回模板对象
temp = loader.get_template('log_pages.html')
# 2. 渲染模板
static_index_html = temp.render(context)

# 生成对应静态文件
save_path = os.path.join(settings.BASE_DIR, 'templates/template_log_pages.html')
with open(save_path, 'w',encoding='utf-8') as f:
    f.write(static_index_html)
