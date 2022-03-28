from django.urls import path
from .import views

urlpatterns = [
    path('', views.loginPage,name="login"),
    path('login/', views.loginPage,name="login"),
    path('logout/', views.logoutUser,name="logout"),
    path('home/', views.home,name="home"),
    path('register/', views.register,name="register"),
]