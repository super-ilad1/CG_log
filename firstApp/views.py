# coding=UTF-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import sys
import json
from django.core.cache import cache

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
import random
from django.urls import reverse
from django.views import View
import re

# sys.path.append(r"D:\PycharmProject\CG_log_web\firstApp")
# 包的根目录
from my_mysql_ORM import *

a = doMysql()


class first(View):  # 这里必须要继承View这个类，只有继承了这个url那里的as_view()才会有这个方法

    def get(self, request, page=None):
        # 默认为89...这个代号
        if page == None:
            selected_unit = (str(897106),)
        else:
            selected_unit = (str(page),)

        print("selected_unit:", selected_unit)

        # 根据ID来选择指定post
        object = a.DoMysql(
                "select * from (select Unit,trans_title,author,date,trans_content,author_alias,portrait FROM c4d_url  inner join c4d_content on c4d_content.post_ID=c4d_url.post_ID where c4d_url.trans_title is not null) as  b where Unit=(%s) ",
            selected_unit)
        title = object[0][1]
        print(title)

        # <editor-fold desc="推荐栏链接提取，从所有available的链接中提取">

        # 没有设置缓存，则设置缓存

        if not cache.get("home_data",None):
            print("No cache")
            # 查询
            filter = lambda x: '/post/' + re.findall('https://forums.creativecow.net/thread/19/(\d+)', x)[0]
            recommen_list = a.DoMysql(
                "select URL,trans_title from c4d_url where trans_title is not null and trans_title like '%?'")
            recommen_list = [{'url': filter(item[0]), 'title': item[1]} for item in recommen_list]

            cache.set("home_data",recommen_list,timeout=60*60)

        recommen_list=cache.get("home_data")


        random.shuffle(recommen_list)
        recommen_list = recommen_list[0:20]

        # </editor-fold>

        trans_content = [{'content': item[4], 'author': item[5], 'date': item[3], 'portrait': item[6],
                          "upvote": random.randint(0, 5)} for item in
                         object]

        intros = trans_content[0]
        print(intros)

        trans_content = trans_content[1:]
        print(trans_content)

        return render(request, 'first.html', context={'title': json.dumps(title), "intros": json.dumps(intros),
                                                      'content': json.dumps(trans_content),
                                                      'recommend_list': recommen_list})

    def post(self, request):
        page = reverse("ask_page", kwargs={'page': '111'})
        print(page)
        return HttpResponse('cbv-post')

# page意味着你的页数，（从url中携带的信息)
def logs(request,page=1):

    # 如果不是首页
    if page !=1:

        if not cache.get("home_data"):
            # 查询
            filter = lambda x: '/post/' + re.findall('https://forums.creativecow.net/thread/19/(\d+)', x)[0]
            recommen_list = a.DoMysql(
                "select URL,trans_title from c4d_url where trans_title is not null and trans_title like '%?'")
            recommen_list = [{'url': filter(item[0]), 'title': item[1]} for item in recommen_list]

            cache.set("home_data",recommen_list,timeout=60*60)

        recommen_list=cache.get("home_data")

        # 分页paginator making,recommen_list是一个[{}]样式的列表
        # 10意味着一个页面有10个数据单位显示
        paginator = Paginator(recommen_list, 10)
        # page是页面数，page_span意味着当你你的分页导航的隔壁页数显示，你不可能只有下一页和上一页
        page_span=[page-2,page-1,page,page+1,page+2]

        # 获取你指定页数的数据（从paginator中）
        try:

            page = paginator.page(page)
        except:
            pass

        return render(request, 'log_pages.html', context={'data': page,'page_span':page_span})

    # 如果是首页，则加载静态的
    else:

        return render(request,'template_log_pages.html')


if __name__ == '__main__':
    # 仅以一个对象为试验
    title = a.DoMysql("select trans_title FROM c4d_url where URL = (%s) ",
                      ('https://forums.creativecow.net/thread/19/896573',))
    title = title[0][0]
    print(title)
    trans_content = a.DoMysql("select trans_content,author,date FROM c4d_content where from_url = (%s) ",
                              ('https://forums.creativecow.net/thread/19/896573',))
    # json对象

    # 第一个dict对象为intro
    trans_content = [{'content': item[0], 'author': item[1], 'date': item[2]} for item in trans_content]
    print(trans_content)
