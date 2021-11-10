from django.urls import path
from .import views as app_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',app_views.index,name='index'),
    path('add_todo',app_views.add_todo,name='add_todo'),
    path('update_todo/<int:todo_id>', app_views.update_todo,name='update_todo'),
    path('delete_todo/<int:todo_id>', app_views.delete_todo,name='delete_todo'),
    path('todo_details/<int:todo_id>',app_views.todo_details,name='todo_details'),
    path('search',app_views.search,name='search'),

]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)