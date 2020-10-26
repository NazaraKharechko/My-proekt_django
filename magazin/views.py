from django.shortcuts import render, redirect
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import LoginForm, UserCreationForm, BayForm
from .models import GoodsModel, TypeModel, BayGoodsModel
from .serializer import GoodsSerializers

Users = get_user_model()


def all_goods(request):
    goods = GoodsModel.objects.all()
    return render(request, 'all_goods.html', {'goods': goods})


def types_goods(request):
    types = TypeModel.objects.all()
    return render(request, 'base.html', {'types': types})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('all/')
                else:
                    return HttpResponse('Authenticated successfully')
            else:
                return redirect('all/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            #  form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password, email=email)
            print(form.data)
            p = User(username=username, email=email, password=password)
            p.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def car_goods(request):
    goods = GoodsModel.objects.filter(type_id=3)
    return render(request, 'car_goods.html', {'goods': goods})


def electronics_goods(request):
    goods = GoodsModel.objects.filter(type_id=1)
    return render(request, 'electronics_goods.html', {'goods': goods})


def sport_goods(request):
    goods = GoodsModel.objects.filter(type_id=8)
    return render(request, 'sport_goods.html', {'goods': goods})


def art_goods(request):
    goods = GoodsModel.objects.filter(type_id=9)
    return render(request, 'art_goods.html', {'goods': goods})


def bay_goods(request):
    if request.method == 'POST':
        form = BayForm(data=request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('city')
            street = form.cleaned_data.get('street')
            house = form.cleaned_data.get('house')
            apartment = form.cleaned_data.get('apartment')
            delivery = form.cleaned_data.get('delivery')

            purchase = BayGoodsModel(city=city, street=street, house=house, apartment=apartment, delivery=delivery)
            HttpResponse('Покупка створина Дякую__)')
            return purchase.save()
    else:
        form = BayForm()
    return render(request, 'bay.html', {'form': form})


class DetailView(CreateAPIView, ListModelMixin):
    serializer_class = GoodsSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        params = self.request.query_params
        id = params.get('id', None)
        if not id:
            return GoodsModel.objects.all()
        return GoodsModel.objects.filter(id=id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
