from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    BusinessListView, 
    ContactListView, 
    NeighborhoodListView,
    PostCreateView,
    BusinessCreateView, 
    ContactCreateView, 
    NeighborhoodCreateView,
    PostUpdateView,
    BusinessUpdateView, 
    ContactUpdateView, 
    NeighborhoodUpdateView,
    PostDeleteView,
    BusinessDeleteView, 
    ContactDeleteView, 
    NeighborhoodDeleteView,
)
from . import views

urlpatterns=[
    path('', PostListView.as_view(), name='index'),
    # Display Views
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('business/', BusinessListView.as_view(), name='business'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('neighborhoods/', NeighborhoodListView.as_view(), name='neighborhoods'),

    # Create Views
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('business/new/', BusinessCreateView.as_view(), name='business-create'),
    path('contact/new/', ContactCreateView.as_view(), name='contact-create'),
    path('neighborhood/new/', NeighborhoodCreateView.as_view(), name='neighborhood-create'),

    # Update Views
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('business/<int:pk>/update/', BusinessUpdateView.as_view(), name='business-update'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
    path('neighborhood/<int:pk>/update/', NeighborhoodUpdateView.as_view(), name='neighborhood-update'),

    # Delete Views
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('business/<int:pk>/delete/', BusinessDeleteView.as_view(), name='business-delete'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),
    path('neighborhood/<int:pk>/delete/', NeighborhoodDeleteView.as_view(), name='neighborhood-delete'),
]