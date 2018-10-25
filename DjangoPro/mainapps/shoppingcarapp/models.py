from django.db import models

#所属用户模型
class Userinfo(models.Model):

    name = models.CharField(max_length=20,verbose_name='用户名')
    sex = models.CharField(max_length=10,blank=True,verbose_name='性别')
    tel_num = models.IntegerField(verbose_name='电话')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_userinfo'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

#购物车模型
class Shoppingcar(models.Model):

    goods_name = models.CharField(max_length=20,verbose_name='商品名称')
    goods_count = models.IntegerField(verbose_name='商品数量')
    goods_price = models.FloatField(verbose_name='商品价格')
    goods_cover =models.ImageField(upload_to='goods',blank=True,null=True,verbose_name='商品封面')
    # 用户购物车关系 一对一
    belong_user = models.OneToOneField(Userinfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.goods_name

    class Meta:
        db_table = 't_car'
        verbose_name = '购物车商品'
        verbose_name_plural = verbose_name

#订单模型
class Order(models.Model):
    # 自定义字段
    order_num = models.CharField(max_length=50,verbose_name='订单号')
    order_address = models.CharField(max_length=100,verbose_name='收货地址')
    order_price = models.DecimalField(max_digits=8,decimal_places=2,verbose_name='订单金额')
    #用户购物车 一对多关系
    order_user = models.ForeignKey(Userinfo,on_delete=models.CASCADE,
                        max_length=20, verbose_name='所属用户')

    def __str__(self):
        return self.order_num

    class Meta:
        db_table = 't_order'
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name



