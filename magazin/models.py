from django.db import models

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
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

    photo = models.ImageField(upload_to='magazin/img', default='', blank=True)
    name = models.CharField(max_length=20)
    type = models.ForeignKey(TypeModel, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=500, default='', blank=True)

    def __str__(self):
        return self.name

    # users = models.ManyToManyField(Users, related_name='goods')


