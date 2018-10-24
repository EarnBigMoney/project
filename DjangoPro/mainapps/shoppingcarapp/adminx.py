import xadmin
from shoppingcarapp.models import *

#后台显示项
class ShoppingcarAdmin():
    list_disaplay = ['goods_name','goods_count','goods_price','belong_user','goods_cover']

class UserinfoAdmin():
    list_disaplay = ['name','sex','tel_num']

class OrderAdmin():
    list_disaplay = ['order_num', 'order_address', 'order_price', 'order_user']

xadmin.site.register(Shoppingcar,ShoppingcarAdmin)
