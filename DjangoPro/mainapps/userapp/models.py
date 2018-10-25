# from django.db import models
# from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class User(models.Model):
#     username = models.CharField(max_length=20,verbose_name='姓名')
#     password = models.IntegerField(verbose_name='密码')
#     email = models.EmailField(verbose_name='邮箱')
#     address = models.CharField(max_length=30,verbose_name='地址')
#     account = models.DecimalField(verbose_name='账户',
#                                   max_digits=10,
#                                   decimal_places=2)

class User(AbstractUser):

    class Meta:
        db_table = 't_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


