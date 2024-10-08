# Generated by Django 2.0 on 2020-02-14 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_auto_20200214_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c4d_content',
            name='Unit',
            field=models.IntegerField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='c4d_content',
            name='author',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='c4d_content',
            name='author_alias',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='c4d_content',
            name='data',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='c4d_content',
            name='from_url',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='c4d_content',
            name='portrait',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='c4d_content',
            name='trans_content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='c4d_content',
            name='upvode',
            field=models.IntegerField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='c4d_url',
            name='trans_title',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
