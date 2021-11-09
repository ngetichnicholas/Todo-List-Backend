from rest_framework import fields, serializers
from .models import TodoNote

class TodoSerializer(serializers.ModelSerializer):
    date_due=serializers.DateField(format=None,input_formats=None)
    class Meta:
        model = TodoNote
        fields = '__all__'