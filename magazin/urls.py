from django.urls import path
from . import views
from .views import all_goods, DetailView

urlpatterns = [
    path('', views.all_goods),
    path('login/', views.user_login, name='login'),
    path('detail/', DetailView.as_view()),
]
