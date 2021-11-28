from django.conf.urls import url
from django.contrib import admin
from app import views


urlpatterns = [
    url(r'^$',views.index,name= 'index'),
    url(r'^search/', views.search_results, name='search_results'),

]

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
# ]