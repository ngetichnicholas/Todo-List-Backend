from django.urls import path
from .import views as api_views

urlpatterns = [ 
    path('',api_views.index,name="index"),
    path('todo_list',api_views.todo_list,name="todo_list"),
    path('todo_details/<int:pk>',api_views.todo_details,name="todo_details"),
    path('add_todo',api_views.add_todo,name="add_todo"),
    path('update_todo/<int:pk>',api_views.update_todo,name="update_todo"),
    path('delete_todo/<int:pk>',api_views.delete_todo,name="delete_todo"),
]