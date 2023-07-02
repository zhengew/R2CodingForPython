"""
URL configuration for templatetest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('tags/', views.tags),
    path('login/', views.csrf_token_login),


    # 模版继承
    path('base/', views.base),
    path('menu1/', views.menu1),
    path('menu2/', views.menu2),
    path('menu3/', views.menu3),

    # 组件
    # 组件
    path('nav/', views.nav),
    path('newpro/', views.newpro),

]
