

from django.shortcuts import render


def go(request):

    return render(request, 'userapp/account.html')
