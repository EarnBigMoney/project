from django.conf.urls import url

from bookapp import views

urlpatterns = [
    url(r'^good/',views.go,name='go')
]
