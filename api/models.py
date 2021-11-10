from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
COMPLETE_CHOICES = (
    ('Yes','Yes'),
    ('No','No')
)

CATEGORY_CHOICES = (
    ('General','General'),
    ('Body Exercise','Body Exercise'),
    ('Learning','Learning'),
    ('Chores','Chores')
)
    
class TodoNote(models.Model):
    title = models.CharField(max_length=250)
    note = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField()
    complete = models.CharField(max_length=5,choices=COMPLETE_CHOICES)
    category = models.CharField(default="General",max_length=20,choices=CATEGORY_CHOICES)
    
    class Meta:
        ordering = ["-date_created"]
        
    def __str__(self):
        return self.title
    
    def save_todo(self):
        self.save()

    def delete_todo(self):
        self.delete()
        
    @classmethod
    def search_todos(cls, todo):
        return cls.objects.filter(title__icontains=todo).all()
