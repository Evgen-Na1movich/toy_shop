from django.urls import path

from toys.views import index, categories, categories_by_slug

urlpatterns = [
    path('', index),
    path('cats/<int:cat_id>/', categories), #http://127.0.0.1:8000/cats/int/
    path('cats/<slug:cat_slug>/', categories_by_slug), #http://127.0.0.1:8000/cats/slug/
]