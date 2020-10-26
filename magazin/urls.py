from django.urls import path
from . import views
from .views import all_goods, DetailView, car_goods, electronics_goods, sport_goods, art_goods, bay_goods

urlpatterns = [
    path('all/', views.all_goods),
    path('', views.user_login, name='login'),
    path('detail/', DetailView.as_view()),
    path('signup/', views.signup, name='signup'),
    path('all/car_goods/', views.car_goods, name='car_goods'),
    path('all/electronics_goods/', views.electronics_goods, name='electronics_goods'),
    path('all/sport_goods/', views.sport_goods, name='sport_goods'),
    path('all/art_goods/', views.art_goods, name='art_goods'),
    path('bay/', views.bay_goods, name='bay_goods'),
]
