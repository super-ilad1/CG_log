# Generated by Django 2.0 on 2020-02-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0003_auto_20200214_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c4d_content',
            name='post_ID',
            field=models.IntegerField(max_length=11, null=True),
        ),
    ]
