from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt

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
    post_date = models.DateTimeField(auto_now_add=True,null=True)


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
        today = dt.date.today()
        images = photos.objects.all(post_date__date = today)
        return images
    
    @classmethod
    def search_by_category(cls,search_term):
        app = cls.objects.filter(category__name__icontains=search_term)
        return app

    @classmethod
    def filter_by_location(cls, location):
        images = photos.objects.filter(location__name=location)
        return images


    @classmethod
    def search(cls, search_term):
        images_by_category = cls.search_by_category(search_term)
        images_by_location = cls.filter_by_location(search_term)
        return images_by_category.union(images_by_location)