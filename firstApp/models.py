from django.db import models


class c4d_url(models.Model):
    #在django中会默认生成可以不用写这行

    post_ID=models.AutoField(primary_key=True,null=False)
    URL=models.TextField()
    title=models.CharField(max_length=1000)
    replies=models.IntegerField()
    if_scrapied=models.CharField(max_length=30,null=True)
    trans_title=models.CharField(max_length=1000,null=True)
    # 修改数据库名字
    class Meta():
        db_table='C4D_url'


class c4d_content(models.Model):

    content_ID=models.AutoField(primary_key=True,null=False)
    content=models.TextField()
    author=models.CharField(max_length=45,null=True)
    date=models.CharField(max_length=80,null=True)
    from_url=models.CharField(max_length=150,null=True)
    Unit=models.IntegerField(null=True)
    trans_content=models.TextField(null=True)
    upvode=models.IntegerField(null=True)
    author_alias=models.CharField(max_length=45,null=True)
    portrait=models.CharField(max_length=200,null=True)
    post_ID=models.IntegerField(null=True)

    # 修改数据库名字
    class Meta():
        db_table='c4d_content'