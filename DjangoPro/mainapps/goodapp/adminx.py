import xadmin
from goodapp.models import Goods

#后台显示项
class Good():
    list_disaplay = ['product_title','product_desc','product_prices','product_cover']

xadmin.site.register(Goods,Good)

