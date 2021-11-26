from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class photos(models.Model):
    # title field
    image = CloudinaryField('image')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    # lo = models.ForeignKey()
    
