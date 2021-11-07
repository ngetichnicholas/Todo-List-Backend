from django.test import TestCase,Client
from .models import TodoNote,Category
import json
from rest_framework import status
from django.urls import reverse
from .serializers import TodoSerializer

# initialize the APIClient app
client = Client()

# Create your tests here.
class TodoNoteTest(TestCase):
    """ Test module for models """

    def setUp(self):
        
        test_category=Category.objects.create(name='Testing')
        
        TodoNote.objects.create(
            title='Back end', note='Create Django Application', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete=False,category=test_category)
        TodoNote.objects.create(
            title='Front end', note='Create VueJS Application', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete=True,category =test_category)

    def test_todo(self):
        todo_note = TodoNote.objects.get(title='Back end')
        note = TodoNote.objects.get(title='Front end')
        category = Category.objects.get(name='Testing')
        self.assertEqual(
            todo_note.title, "Back end")
        
        self.assertEqual(
            note.title, "Front end")
        
        self.assertEqual(
            category.name, 'Testing'
        )
        
class GetAllTodoTest(TestCase):
    """ Test module for GET all Todo API """

    def setUp(self):
        test_category=Category.objects.create(name='Testing')
        
        TodoNote.objects.create(
            title='Back end', note='Create Django Application', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete=False,category=test_category)
        
        TodoNote.objects.create(
            title='New Test', note='New testing note', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete=False,category=test_category)
        TodoNote.objects.create(
            title='Hello Test', note='Hello world test case', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete=True,category =test_category)


    def test_get_all_todo(self):
        # get API response
        response = client.get(reverse('index'))
        # get data from db
        todo = TodoNote.objects.all()
        serializer = TodoSerializer(todo, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
