from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_add_book')
def add_book_view(request):
    # your add book logic

@permission_required('relationship_app.can_change_book')
def edit_book_view(request, book_id):
    # your edit book logic

@permission_required('relationship_app.can_delete_book')
def delete_book_view(request, book_id):
    # your delete book logic
