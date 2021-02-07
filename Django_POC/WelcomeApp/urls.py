from . import views

from django.urls import path

urlpatterns = [
    path('', views.homePage, name = "homePage"),
    path('index/', views.homePage, name = "homePage"), # we can remove this line if you want
    path('add/' , views.addContent, name = 'contribute'),
    path('<str:queryName>/', views.findPage, name = "findPage")
    
]