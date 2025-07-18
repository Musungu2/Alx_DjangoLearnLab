from django.urls import path
from .views import book_list, LibraryDetailView
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Registration
    path('registration/', user_views.register, name='registration'),
]