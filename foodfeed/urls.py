from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.main, name="main page"),
    path('main/', views.main, name="main page"),
    path('card', views.card, name="card page"),
    path('<animal_name>/', views.animal_name),
    path('<animal_name>/<animal_item>/', views.animal_item),
    path('<animal_name>/<animal_item>/<item_type>/', views.food_type),
    path('<animal_name>/<animal_item>/<item_type>/<food_name>', views.food),
]