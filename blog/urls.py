from django.urls import path 
from .views import BlogCreateView , BlogDetailsView , BlogUpdateView , BlogDeleteView ,TagcreateView , CategorycreateView , SearchView

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('details/<int:id>/',BlogDetailsView.as_view(), name='details'),
    path('update/<int:id>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', BlogDeleteView.as_view(), name='delete'),
    path('tag/create/', TagcreateView.as_view(), name='tagcreate'),
    path('category/create/', CategorycreateView.as_view(), name='categorycreate'),
    path('search/', SearchView.as_view(), name='search'),
]
