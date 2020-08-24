from django.urls import path
from . import views
from .views import all_goods

urlpatterns = [
    path('', views.all_goods)
]
