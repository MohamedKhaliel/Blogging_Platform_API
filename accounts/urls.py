from django.urls import path 
from . views import UserRegistrationView , UserLoginView , UserListView , UserProfileUpdateView 

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='users'),
    path('update/<int:user_id>', UserProfileUpdateView.as_view(), name='update'),
]