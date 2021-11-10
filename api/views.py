from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TodoSerializer
from .models import TodoNote

# Create your views here.
@api_view(['GET'])
def index(request):
    api_endpoints = {
        'List': '/todo_list',
        'Todo Details': '/todo_details/<int:pk>/',
        'Create': '/add-todo/',
        'Update': '/update_todo/<int:pk>/',
        'Delete': '/delete_todo/<int:pk>/',
        
    }
    return Response(api_endpoints)

@api_view(['GET'])
def todo_list(request):
    todo = TodoNote.objects.all()
    serializer = TodoSerializer(todo,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def todo_details(request,pk):
    
    try:
        todo = TodoNote.objects.get(pk=pk)
    except TodoNote.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TodoSerializer(todo)
    return Response(serializer.data)

@api_view(['POST'])
def add_todo(request):
    serializer = TodoSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_todo(request,pk):
    try:
        todo = TodoNote.objects.get(pk=pk)
    except TodoNote.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TodoSerializer(todo, data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_todo  (request,pk):
    try:
        todo = TodoNote.objects.get(id=pk)
    except TodoNote.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    todo.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)