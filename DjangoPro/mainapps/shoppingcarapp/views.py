# https://blog.csdn.net/huangzhang_123/article/details/73733836

from django.shortcuts import render

def show(request):
    return render(request,'account.html',locals())


