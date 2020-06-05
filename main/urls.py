from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),#url to home page
    path('<int:id>', views.home, name="todo"),
    path('connect/', views.connect, name="connect"),
    path('addTo/', views.addTo, name="add"),#form view for add
    path('deleteTo/<int:todo_id>', views.deleteTo, name="delete"),#form view for delete
]
