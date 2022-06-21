from django.shortcuts import render
from .models import Post, Business, Contact, Neighborhood
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
)

# Create your views here.
def index(request):
    title='Home'
    return render(request, 'index.html', {'title': title})


class PostListView(ListView):
    model = Post
    template_name = 'index.html' # Expected </app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'description', 'post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.neighborhood = self.request.user.profile.neighborhood
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html' 



class BusinessListView(ListView):
    model = Business
    template_name = 'business.html' # Expected </app>/<model>_<viewtype>.html
    context_object_name = 'businesses'
    ordering = ['-date_created']


class BusinessCreateView(CreateView):
    model = Business
    fields = ['name', 'email_address', 'business_image']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.neighborhood = self.request.user.profile.neighborhood
        return super().form_valid(form)




class ContactListView(ListView):
    model = Contact
    template_name = 'contact.html' # Expected </app>/<model>_<viewtype>.html
    context_object_name = 'contacts'
    ordering = ['-date_posted']


class ContactCreateView(CreateView):
    model = Contact
    fields = ['title', 'description', 'phone_number', 'email_address']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.neighborhood = self.request.user.profile.neighborhood
        return super().form_valid(form)



class NeighborhoodCreateView(CreateView):
    model = Post
    fields = ['name', 'location', 'occupants_count', 'hood_image']

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

