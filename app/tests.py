from django.test import TestCase
from app.models import Location, Category, photos

# Create your tests here.
class PhotosTestClass(TestCase):
    def setUp(self):
        """
        Create a image for testing
        """
        photos.objects.create(
            title="Photo Test",
            description="Description Test",
            location=Location.objects.create(name="Location Test"),
            category=Category.objects.create(name="Category Test"),
            image="http://test.com/test.jpg",
            date_posted=None
        )




# category models test
class CategoryTestCase(TestCase):

    def setUp(self):
        """
        Create a category for testing
        """
        Category.objects.create(name="Photo Category")
        
    def test_category_name(self):
        """
        Test that the category name is correct
        """
        category = Category.objects.get(name="Photo Category")
        self.assertEqual(category.name, "Photo Category")

    def test_category_str(self):
        """
        Test that the category string representation is correct
        """
        category = Category.objects.get(name="Photo Category")
        self.assertEqual(str(category), "Photo Category")

# location model tests
class LocationTestCase(TestCase):

    def setUp(self):
        """
        Create a setup for testing locaation
        """
        Location.objects.create(name="Photo Location")
    
    def test_location_name(self):
        """
        Test that the location name is correct
        """
        location = Location.objects.get(name="Photo Location")
        self.assertEqual(location.name, "Photo Location")
        
    def test_location_str(self):
        """
        Test that the location string representation is correct
        """
        location = Location.objects.get(name="Photo Location")
        self.assertEqual(str(location), "Photo Location")
