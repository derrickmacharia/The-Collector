from django.test import TestCase
from app.models import Location, Category, photos

# Create your tests here.
class PhotosTestClass(TestCase):
    def setUp(self):
        """
        Create a image for testing
        """
        photos.objects.create(
            title="Image Test",
            description="Description Test",
            location=Location.objects.create(name="Location Test"),
            category=Category.objects.create(name="Category Test"),
            image="http://test.com/test.jpg",
            created_at=None
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


