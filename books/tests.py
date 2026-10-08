from django.test import TestCase
from books.models import book

# Create your tests here.



class BookTestCase(TestCase):
    def setUp(self):
        book.objects.create(title="harry potter", author="Joane Rowling")

    def test_animals_can_speak(self):
        harry = book.objects.get(title="harry potter")
        self.assertEqual(harry.info(), f"The {harry.title} book was written by {harry.author}")

        harry.title = "Princess"
        harry.save(update_fields=["title"])
        self.assertEqual(harry.info(), f"The {harry.title} book was written by {harry.author}")