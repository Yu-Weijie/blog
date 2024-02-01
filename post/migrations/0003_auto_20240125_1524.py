# Generated by Django 3.2.23 on 2024-01-25 07:24

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20240124_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='文章内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发帖时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='describe',
            field=models.CharField(max_length=128, verbose_name='文章描述'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=32, unique=True, verbose_name='文章标题'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tname',
            field=models.CharField(max_length=32, unique=True, verbose_name='标签名称'),
        ),
    ]
