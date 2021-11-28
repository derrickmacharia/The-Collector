from django.test import TestCase
from app.models import Location, Category, photos

# Create your tests here.
class PhotosTestClass(TestCase):
    def setUp(self):
        """
        Create a image for testing
        """
        photos.objects.create(
            title="Test Image",
            description="Test Description",
            location=Location.objects.create(name="Test Location"),
            category=Category.objects.create(name="Test Category"),
            image="http://test.com/test.jpg",
            created_at=None
        )
