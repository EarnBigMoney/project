

from django.conf.urls import url,include
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
]


