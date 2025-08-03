# Django Admin Setup for Book Model

## Admin Registration
Registered the `Book` model using `@admin.register(Book)` in `bookshelf/admin.py`.

## Customizations
- **list_display**: Shows `title`, `author`, and `publication_year` in admin list view.
- **list_filter**: Allows filtering books by `publication_year`.
- **search_fields**: Enables searching by `title` and `author`.

## Screenshot (optional)
_Add a screenshot of the admin panel here if needed._

## Access
URL: http://127.0.0.1:8000/admin  
Login with your superuser credentials.
``