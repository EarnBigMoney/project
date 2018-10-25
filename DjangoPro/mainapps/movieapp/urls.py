from django.conf.urls import url

from movieapp import views

urlpatterns = [
    url(r'^go/',views.go,name='go')
]