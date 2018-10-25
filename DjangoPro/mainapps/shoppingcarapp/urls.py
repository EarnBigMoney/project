from django.conf.urls import url

from shoppingcarapp import views

urlpatterns = [
    url(r'^go/',views.go,name='go')
]