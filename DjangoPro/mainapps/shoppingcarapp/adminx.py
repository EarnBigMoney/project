import xadmin
from shoppingcarapp.models import *

#后台显示项
class ShoppingcarAdmin():
    list_disaplay = ['goods_name','adress','goods_count','goods_price','belong_user','goods_cover','is_delete']

class UserinfoAdmin():
    list_disaplay = ['name','sex','tel_num','is_delete']

class OrderAdmin():
    list_disaplay = ['order_num', 'order_address', 'order_price','order_user','is_delete']

xadmin.site.register(Shoppingcar,ShoppingcarAdmin)
