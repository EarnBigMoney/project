from django.shortcuts import render
from goodapp.models import Goods

def goodsinfo(request):
    goodsinfo = Goods.objects.get()
    return render(request,'',locals())


