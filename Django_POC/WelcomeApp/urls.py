from . import views

from django.urls import path

urlpatterns = [
    path('', views.homePage, name = "homePage"),
    path('<str:queryName>/', views.findPage, name = "findPage")
    
]
// Test