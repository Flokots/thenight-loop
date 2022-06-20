from django.shortcuts import render
from .models import Post, Business, Contact, Neighborhood
from django.views.generic import ListView

# Create your views here.
def index(request):
    title='Home'
    return render(request, 'index.html', {'title': title})


class PostListView(ListView):
    model = Post
    template_name = 'index.html' # Expected </app>/<model>_<viewtype>.html
    context_object_name = 'posts'

