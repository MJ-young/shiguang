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

from django.urls import path
from ShiGuang import views
urlpatterns = [
    path('login/', views.login),
    path('getfood/', views.getfood),
    path('search/', views.search),
    path('searchByPage/', views.searchByPage),
    path('findByInput/', views.findByInput),
    path('sportByPage/', views.sportByPage),
    path('findSportByInput/', views.findSportByInput),
    path('addFoodRecord/', views.addFoodRecord),
    path('addSportRecord/', views.addSportRecord),
    path('RecordByDate/', views.RecordByDate),
    path('DelRecard/', views.DelRecard),
    path('addSport/', views.addSport),
    path('addFood/', views.addFood),
    path('delSport/', views.delSport),
    path('delFood/', views.delFood),
    path('propose/', views.propose),
    path('getListByPage/', views.getListByPage),
    path('edit/', views.edit),
    path('delByid/', views.delByid)
]
