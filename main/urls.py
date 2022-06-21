from django.urls import path
from .views import PostListView, PostDetailView, BusinessListView, ContactListView
from . import views

urlpatterns=[
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('business/', BusinessListView.as_view(), name='business'),
    path('contacts/', ContactListView.as_view(), name='contacts'),

]