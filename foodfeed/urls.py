from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.main, name="main page"),
    path('main/', views.main, name="main page"),
    path('<animal_name>/', views.animal_name),
    path('<animal_name>/<animal_item>/', views.animal_item),
]