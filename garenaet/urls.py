from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/', views.login, name='login'),
    url(r'profile/', views.profile, name='profile'),
    url(r'update/nickname/', views.update_nickname, name='update_nickname'),
    url(r'check/token/', views.check_token, name='check_token')
]