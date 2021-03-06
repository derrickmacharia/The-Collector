from django.test import TestCase
from app.models import Location, Category, photos

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
            post_date=None
        )

    def test_images_name(self):
        """
        Test that the image name is correct
        """
        image = photos.objects.get(title="Photo Test")
        self.assertEqual(image.title, "Photo Test")
    
    def test_images_description(self):
        """
        Test that the image description is correct
        """
        image = photos.objects.get(title="Photo Test")
        self.assertEqual(image.description, "Description Test")

    def test_photos_location(self):
        """
        Test that the image location is correct
        """
        image = photos.objects.get(title="Photo Test")
        self.assertEqual(image.location.name, "Location Test")
    
    def test_photos_category(self):
        """
        Test that the image category is correct
        """
        image = photos.objects.get(title="Photo Test")
        self.assertEqual(image.category.name, "Category Test")
    
    def test_photos_str(self):
        """
        Test that the image string representation is correct
        """
        image = photos.objects.get(title="Photo Test")
        self.assertEqual(str(image), "Photo Test")


# category models test
