from django.test import TestCase
from .models import TodoNote,Category

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
        
