"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from ShiGuang import views as view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("ShiGuang.urls")),
    path('login/',view.login),
    path('regist/',view.regist),
    # 访问注册界面
    # http://127.0.0.1:8000/userRegist/，会执行views中Usercontrller的regist方法，下一个相同的道理
    path('userRegist/', view.UserController.userRegist),
    path('userLogin/', view.UserController.userLogin),
    # http://127.0.0.1:8000/userinfo/{这里需要一个整形参数，参数命名为id}/，这样的url会执行views中Usercontrller的userInfo方法，
    path('userinfo/<int:id>', view.UserController.userInfo)
]
