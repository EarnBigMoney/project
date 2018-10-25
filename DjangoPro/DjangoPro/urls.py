
"""DjangoPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.shortcuts import render

import xadmin

def index(request):

    return render(request,'index.html')

urlpatterns = [

    url(r'^xadmin/', xadmin.site.urls),
    url(r'^goods/',include('goodapp.urls',namespace='good')),
    url(r'^book/',include('bookapp.urls',namespace='book')),
    url(r'^movie/',include('movieapp.urls',namespace='movie')),
    url(r'^car/',include('shoppingcarapp.urls',namespace='car')),
    url(r'^index/',index)
]


