from django.db import models

# Create your models here.
STATUS_CHOICES = (
    ('Completed','Completed'),
    ('Pending','Pending')
)

CATEGORY_CHOICES = (
   ('General','General'),
   ('Work','Work'),
   ('Personal','Personal'),
   ('Health','Health'),
   ('Shopping','Shopping'),
   ('Education','Education'),
   ('Entertainment','Entertainment'),
   ('Others','Others')
)

    
class TodoNote(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField()
    status = models.CharField(max_length=50,choices=STATUS_CHOICES)
    category = models.CharField(default="General",max_length=50,choices=CATEGORY_CHOICES)
    
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
