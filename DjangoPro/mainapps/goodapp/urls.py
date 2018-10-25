from django.conf.urls import url
from goodapp import views

urlpatterns = [
    url(r'^goods/',views.goodsinfo)
]


