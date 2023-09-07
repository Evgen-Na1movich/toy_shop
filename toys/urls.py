from django.urls import path

from toys.views import index, Login, Register, logout_func, CategoriesView

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000/
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', logout_func, name='logout'),
    path('cats/', CategoriesView.as_view, name='index'),
]
