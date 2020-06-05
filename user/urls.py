from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path('register/', views.register, name="register"),#url to register user
    path('login/', views.signin, name="login"),#url to login user
    path('logout/', views.signout, name="logout"),#url to logout user
]
