from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns=[
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

]