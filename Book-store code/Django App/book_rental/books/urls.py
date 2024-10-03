from django.urls import path
from .views import book_list, rent_book, return_book, add_book, delete_book

urlpatterns = [
    path('', book_list, name='book_list'),
    path('add/', add_book, name='add_book'),  # Add book view
    path('delete/<str:title>/', delete_book, name='delete_book'),  # Delete book view
    path('rent/<str:title>/', rent_book, name='rent_book'),  # Change to accept title
    path('return/<str:title>/', return_book, name='return_book'),
]
