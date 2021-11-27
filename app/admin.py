from django.contrib import admin
from .models import Category, Location, photos

# class photosAdmin(admin.ModelAdmin):
#     filter_horizontal =('category',)

admin.site.register(photos)
admin.site.register(Category)
admin.site.register(Location)