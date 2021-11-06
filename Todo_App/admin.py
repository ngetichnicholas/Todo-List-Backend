from django.contrib import admin
from .models import TodoNote,Category

# Register your models here.
admin.site.register(TodoNote)
admin.site.register(Category)
