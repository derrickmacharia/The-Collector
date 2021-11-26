from django.conf.urls import url
from django.contrib import admin
from app import views


urlpatterns = [
    url(r'^$',views.index,name= 'index')

]

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
# ]