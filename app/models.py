from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

# Create your models here.
class photos(models.Model):
    # title field
    image = CloudinaryField('image')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

    def save_photos(self):
        self.save()

    # update image
    def update_photos(self, title, description, category,location):
        self.title = title
        self.description = description
        self.location = location
        self.category = category
        self.save()

    # get all images
    @classmethod
    def get_all_photos(cls):
        images = photos.objects.all()
        return images
    
    @classmethod
    def search_by_category(cls,search_term):
        app = cls.objects.filter(category__name__icontains=search_term)
        return app

    @classmethod
    def filter_by_location(cls, location):
        images = photos.objects.filter(location__name=location)
        return images

