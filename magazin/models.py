from django.db import models

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import os

Users = get_user_model()


class TypeModel(models.Model):
    class Meta:
        db_table = 'type_goods'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типи'
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class GoodsModel(models.Model):
    class Meta:
        db_table = 'goods'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    photo = models.ImageField(upload_to=os.path.join('magazin', 'img'), default='', blank=True)
    name = models.CharField(max_length=20)
    type = models.ForeignKey(TypeModel, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=500, default='', blank=True)

    def __str__(self):
        return self.name

    # users = models.ManyToManyField(Users, related_name='goods')


class UserProfileRegister(models.Model):
    class Meta:
        db_table = 'user_register'
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class BayGoodsModel(models.Model):
    class Meta:
        db_table = 'bay_goods'

    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    house = models.IntegerField()
    apartment = models.IntegerField()
    delivery = models.BooleanField()


# class Shop(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.PointField()
#     address = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)
