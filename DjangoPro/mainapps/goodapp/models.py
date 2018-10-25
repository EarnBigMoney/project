from django.db import models

#商品模型
class Goods(models.Model):
    product_title = models.CharField(max_length=20,verbose_name='商品名')
    product_desc = models.CharField(max_length=50,verbose_name='商品描述')
    product_prices = models.FloatField(verbose_name='商品价格')
    product_cover = models.ImageField(upload_to='goods',blank=True,null=True,verbose_name='商品封面')
    is_delete = models.IntegerField(default='0',choices=((0,'否'),(1,'是')),verbose_name='是否删除')

    def __str__(self):
        return self.product_title

    class Meta:
        db_table = 't_goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name


