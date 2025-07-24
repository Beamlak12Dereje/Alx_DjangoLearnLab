from django.urls import path
from relationship_app.views import add_book_view, edit_book_view, delete_book_view

urlpatterns = [
    path('books/add/', add_book_view, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book_view, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book_view, name='delete_book'),
]
