# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_src', models.CharField(blank=True, max_length=150, verbose_name='图片地址')),
                ('book_title', models.CharField(blank=True, max_length=20, verbose_name='书籍名称')),
                ('book_author', models.CharField(blank=True, max_length=20, verbose_name='作者')),
                ('book_style', models.CharField(blank=True, max_length=20, verbose_name='类型')),
                ('book_publish', models.CharField(blank=True, max_length=20, verbose_name='出版社')),
                ('book_words', models.CharField(blank=True, max_length=20, verbose_name='字数')),
                ('book_price', models.FloatField(blank=True, max_length=20, verbose_name='全本定价')),
                ('book_pre', models.TextField(blank=True, max_length=1000, verbose_name='导言')),
                ('book_hits', models.IntegerField(verbose_name='点击量')),
                ('is_delete', models.IntegerField(choices=[(0, '否'), (1, '是')], default='0', verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '书籍列表',
                'verbose_name_plural': '书籍列表',
                'db_table': 't_books',
                'ordering': ['-book_hits'],
            },
        ),
    ]