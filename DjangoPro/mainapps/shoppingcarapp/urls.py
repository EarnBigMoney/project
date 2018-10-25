from django.conf.urls import url

from shoppingcarapp import views

urlpatterns = [
    url(r'^car/',views.go,name='go')
]