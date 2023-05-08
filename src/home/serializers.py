from rest_framework import serializers
from .models import History, Total


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('a', 'b')


class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total
        fields = ('total',)