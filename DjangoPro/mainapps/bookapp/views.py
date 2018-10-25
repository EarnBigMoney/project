from django.shortcuts import render
from bookapp.models import Book
# Create your views here.

def Book_show(request):
    return render(request,'category.html',locals())


