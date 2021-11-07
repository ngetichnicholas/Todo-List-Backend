from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=144)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
        
    def __str__(self):
        return self.name
    
class TodoNote(models.Model):
    title = models.CharField(max_length=250)
    note = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField()
    complete = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=CASCADE, default="general")
    
    class Meta:
        ordering = ["-date_created"]
        
    def __str__(self):
        return self.title