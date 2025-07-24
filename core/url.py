from django.urls import path
from relationship_app.views import (
    register,
    admin_dashboard,
    librarian_dashboard,
    member_dashboard,
    home,  # <- add this if you create a home view
)

urlpatterns = [
    path('', home, name='home'),  # root URL directs to home view
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/register/', register, name='register'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),
]
