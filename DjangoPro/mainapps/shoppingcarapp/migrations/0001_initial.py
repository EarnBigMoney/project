# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 13:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.CharField(max_length=50, verbose_name='订单号')),
                ('order_address', models.CharField(max_length=100, verbose_name='收货地址')),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='订单金额')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
                'db_table': 't_order',
            },
        ),
        migrations.CreateModel(
            name='Shoppingcar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=20, verbose_name='商品名称')),
                ('goods_count', models.IntegerField(verbose_name='商品数量')),
                ('goods_price', models.FloatField(verbose_name='商品价格')),
                ('goods_cover', models.ImageField(blank=True, null=True, upload_to='goods', verbose_name='商品封面')),
            ],
            options={
                'verbose_name': '购物车商品',
                'verbose_name_plural': '购物车商品',
                'db_table': 't_car',
            },
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='用户名')),
                ('sex', models.CharField(blank=True, max_length=10, verbose_name='性别')),
                ('tel_num', models.IntegerField(verbose_name='电话')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 't_userinfo',
            },
        ),
        migrations.AddField(
            model_name='shoppingcar',
            name='belong_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shoppingcarapp.Userinfo'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_user',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='shoppingcarapp.Userinfo', verbose_name='所属用户'),
        ),
    ]