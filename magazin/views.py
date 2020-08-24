from django.shortcuts import render, redirect
from .models import GoodsModel


def all_goods(request):
    goods = GoodsModel.objects.all()
    return render(request, 'all_goods.html', {'goods': goods})
