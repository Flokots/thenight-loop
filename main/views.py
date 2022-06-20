from django.shortcuts import render
from .models import Post, Business, Contact, Neighborhood
from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):
    title='Home'
    return render(request, 'index.html', {'title': title})


class PostListView(ListView):
    model = Post
    template_name = 'index.html' # Expected </app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html' 


class BusinessListView(ListView):
    model = Business
    template_name = 'business.html' # Expected </app>/<model>_<viewtype>.html
    context_object_name = 'businesses'
    ordering = ['-date_created']


class ContactListView(ListView):
    model = Contact
    template_name = 'contact.html' # Expected </app>/<model>_<viewtype>.html
    context_object_name = 'contacts'
    ordering = ['-date_posted']
