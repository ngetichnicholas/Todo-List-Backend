from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TodoSerializer
from .models import TodoNote

# Create your views here.
@api_view(['GET'])
def index(request):
    todo = TodoNote.objects.all()
    serializer = TodoSerializer(todo,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def todo_details(request,pk):
    todo = TodoNote.objects.get(id=pk)
    serializer = TodoSerializer(todo,many = False)
    return Response(serializer.data)

@api_view(['POST'])
def add_todo(request):
    serializer = TodoSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update_todo(request,pk):
    todo = TodoNote.objects.get(id=pk)
    serializer = TodoSerializer(instance= todo, data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_todo  (request,pk):
    todo = TodoNote.objects.get(id=pk)
    todo.delete()

    return Response("Todo deleted successfully")