from django.conf.urls import url
from userapp import views

urlpatterns = [
    url(r'^register/',views.RegisterView.as_view(),name='register'),
    # url(r'^active/(?P<token>.*)$',views.ActiveView.as_view(),name='active'),
    url(r'^login/',views.LoginView.as_view(),name='login'),
]