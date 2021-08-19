from rest_framework import serializers

from .models import customers

from django import forms

class customersSerializer(serializers.ModelSerializer):
    class Meta:
        model = customers
        fields = '__all__'