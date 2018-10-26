from django.shortcuts import render,redirect
from django.http import HttpResponse
from userapp.models import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
# from celery_tasks.tasks import send_register_active_email
from DjangoPro import settings
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
import re


# Create your views here.
#user/register


#注册
class RegisterView(View):
    def get(self,request):
        return render(request, "user_app/register.html")
    def post(self,request):
        username = request.POST["user_name"]
        password = request.POST["pwd"]
        email = request.POST["email"]
        allow = request.POST["allow"]
        if not all([username, password, email]):
            return render(request, "user_app/register.html", {"msg": "数据不完整"})
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, "user_app/register.html", {"msg": "邮箱格式不正确"})
        if allow != 'on':
            return render(request,"user_app/register.html",{"msg":"请同意协议"})
        try:
           user = User.objects.get(username=username)
        except User.DoesNotExist:
           user = None
        if user:
           return render(request, "user_app/register.html", {"msg": "该用户名已存在"})
        # serializer = Serializer(settings.SECRET_KEY, 60)

        # info = {"confirm": user.id}
        # token = serializer.dumps(info)
        # token = token.decode()
        # send_register_active_email(email,username,token)

        return render(request,"user_app/user_login.html")

'''
class ActiveView(View):
    def get(self,request,token):
        serializer = Serializer(settings.SECRET_KEY, 60)
        try:
            info = serializer.load(token)
            userid = info["confirm"]
            user = User.objects.get(id=userid)
            user.is_active = 1
            user.save()
        except SignatureExpired as e:
            return HttpResponse("验证码已过期")
'''

#用户登录
class LoginView(View):
    def get(self,request):
        return render(request, "user_app/user_login.html")
    def post(self,request):
        #接收数据
        username = request.POST["username"]
        password = request.POST["passworld"]
        #校验数据
        if not all([username,password]):
            return render(request, "user_app/user_login.html", {"msg": "数据不完整"})
        #登录
        user = User.objects.get(username=username,password=password)
        if user is not None:
            return render(request, "./index.html")
            # if user.is_active:
            #     login(request,user)
            #     return redirect(reverse("good:index"))
            # else:
            # return render(request, "user_app/user_login.html", {"msg": "用户未激活"})
        else:
            return render(request, "user_app/user_login.html", {"msg": "用户名或者密码错误"})
        #返回结果