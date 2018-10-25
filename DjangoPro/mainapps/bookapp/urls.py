from django.conf.urls import url

from bookapp import views

urlpatterns = [
    url(r'^books/',views.go,name='go')
]
