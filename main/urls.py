from django.urls import path
from .views import PostListView, PostDetailView, BusinessListView
from . import views

urlpatterns=[
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('business/', BusinessListView.as_view(), name='business'),

]