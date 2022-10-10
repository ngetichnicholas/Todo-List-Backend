from django.test import TestCase,Client
from .models import TodoNote
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
        
        TodoNote.objects.create(
            title='Back end', note='Create Django Application', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete='No',category='General')
        TodoNote.objects.create(
            title='Front end', note='Create VueJS Application', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete='Yes',category ='General')

    def test_todo(self):
        todo_note = TodoNote.objects.get(title='Back end')
        note = TodoNote.objects.get(title='Front end')
        self.assertEqual(
            todo_note.title, "Back end")
        
        self.assertEqual(
            note.title, "Front end")
        
        
class GetAllTodoTest(TestCase):
    """ Test module for GET all Todo API """

    def setUp(self):
        
        TodoNote.objects.create(
            title='Back end', note='Create Django Application', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete='No',category='General')
        
        TodoNote.objects.create(
            title='New Test', note='New testing note', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete='No',category='General')
        TodoNote.objects.create(
            title='Hello Test', note='Hello world test case', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete='Yes',category ='General')


    def test_get_all_todo(self):
        # get API response
        response = client.get(reverse('todo_list'))
        # get data from db
        todo = TodoNote.objects.all()
        serializer = TodoSerializer(todo, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleTodoTest(TestCase):
    """ Test module for GET single Todo API """

    def setUp(self):
        
        self.back_end=TodoNote.objects.create(
            title='Back end', note='Create Django Application', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete='No',category='General')
        
        self.new_test=TodoNote.objects.create(
            title='New Test', note='New testing note', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete='No',category='General')
        self.hello_test=TodoNote.objects.create(
            title='Hello Test', note='Hello world test case', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete='Yes',category ='General')

    def test_get_valid_single_todo(self):
        response = client.get(
            reverse('todo_details', kwargs={'pk': self.back_end.pk}))
        todo = TodoNote.objects.get(pk=self.back_end.pk)
        serializer = TodoSerializer(todo)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_todo(self):
        response = client.get(
            reverse('todo_details', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
class CreateNewTodoTest(TestCase):
    """ Test module for inserting a new todo """

    def setUp(self):
        
        self.valid_payload =     {
        "id": 3,
        "title": "Test",
        "note": "Create test Note",
        "date_created": "2021-11-11",
        "date_due": "2021-11-11",
        "complete": "Yes",
        "category": "General"
    }
        self.invalid_payload = {
        "id": 1,
        "title": "",
        "note": "Create test Note",
        "date_created": "2021-11-07T20:52:26.727495+03:00",
        "date_due": "2021-11-07T20:51:48+03:00",
        "complete": 'No',
        "category": 'General'
    }

    def test_create_valid_todo(self):
        response = client.post(
            reverse('add_todo'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_todo(self):
        response = client.post(
            reverse('add_todo'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
class UpdateSingleTodoTest(TestCase):
    """ Test module for upating existing todo """

    def setUp(self):
        
        self.back_end=TodoNote.objects.create(
            title='Back end', note='Create Django Application', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete='No',category='General')
        
        self.new_test=TodoNote.objects.create(
            title='New Test', note='New testing note', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete='No',category='General')
        
        self.valid_payload =     {
        "id": 1,
        "title": "Test",
        "note": "Create test Note",
        "date_created": "2021-11-11",
        "date_due": "2021-11-11",
        "complete": "Yes",
        "category": "General"
    }
        self.invalid_payload = {
        "id": 1,
        "title": "",
        "note": "Create test Note",
        "date_created": "2021-11-07T20:52:26.727495+03:00",
        "date_due": "2021-11-07T20:51:48+03:00",
        "complete": 'Yes',
        "category": 'General'
    }

    def test_valid_todo_update(self):
        response = client.put(
            reverse('update_todo', kwargs={'pk': self.new_test.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_todo_update(self):
        response = client.put(
            reverse('update_todo', kwargs={'pk': self.new_test.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleTodoTest(TestCase):
    """ Test module for deleting an existing Todo record """

    def setUp(self):
        
        self.back_end=TodoNote.objects.create(
            title='Back end', note='Create Django Application', date_created='2021-11-07T20:52:26.727495+03:00',date_due='2021-11-07T20:52:26.727495+03:00',complete='No',category='General')

    def test_valid_delete_todo(self):
        response = client.delete(
            reverse('delete_todo', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_todo(self):
        response = client.delete(
            reverse('delete_todo', kwargs={'pk': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)