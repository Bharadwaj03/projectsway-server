from rest_framework import serializers
from .models import ClickUpData

class ClickUpDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClickUpData
        fields = ['id', 'title', 'description']