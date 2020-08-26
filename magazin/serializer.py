from rest_framework import serializers
from .models import GoodsModel


class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsModel
        fields = '__all__'
