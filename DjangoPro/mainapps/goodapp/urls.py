from django.conf.urls import url

from goodapp import views

urlpatterns = [
    url(r'^good/',views.go,name='go')
]
