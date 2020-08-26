from django.shortcuts import render, redirect
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model, authenticate, login
from django.http import HttpResponse
from .forms import LoginForm
from .models import GoodsModel
from .serializer import GoodsSerializers

User = get_user_model()


def all_goods(request):
    goods = GoodsModel.objects.all()
    return render(request, 'all_goods.html', {'goods': goods})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                goods = GoodsModel.objects.all()
                return render(request, 'all_goods.html', {'goods': goods})

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


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
