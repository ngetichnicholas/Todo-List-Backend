from rest_framework import fields, serializers
from .models import TodoNote

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoNote
        fields = '__all__'