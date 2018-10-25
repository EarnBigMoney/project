from django.shortcuts import render
from movieapp.models import Movie
# Create your views here.


def Movie_show(request):

    return render(request,'category.html',locals())