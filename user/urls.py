from django.urls import path
from .import views

urlpatterns = [
    path('', views.loginPage,name="login"),
    path('login/', views.loginPage,name="login"),
    path('logout/', views.logoutUser,name="logout"),
    path('home/', views.home,name="home"),
    path('register/', views.register,name="register"),
    path('book/<str:test_name>/', views.book ,name="book"),
    path('booking-history/', views.history ,name="history"),
    path('profile/', views.profile ,name="profile"),
    path('delete/<int:b_id>', views.cancel ,name="cancel"),
    path('haematology/', views.haematology ,name="haematology"),
]