from django.contrib import admin
from .models import Category, photos

# class photosAdmin(admin.ModelAdmin):
#     filter_horizontal =('category',)

admin.site.register(photos)
admin.site.register(Category)