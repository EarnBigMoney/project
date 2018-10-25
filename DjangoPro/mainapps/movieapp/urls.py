from django.conf.urls import url

from movieapp import views

urlpatterns = [
    url(r'^movies/',views.go,name='go')
]