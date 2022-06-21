from django.shortcuts import render
from .models import Post, Business, Contact, Neighborhood
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
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


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.neighborhood = self.request.user.profile.neighborhood
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




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


class BusinessUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Business
    fields = ['name', 'email_address', 'business_image']

    def form_valid(self, form):   
        form.instance.owner = self.request.user
        form.instance.neighborhood = self.request.user.profile.neighborhood
        return super().form_valid(form)

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.owner:
            return True
        return False


class BusinessDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Business
    success_url = '/'

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.owner:
            return True
        return False



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


class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ['title', 'description', 'phone_number', 'email_address']

    def form_valid(self, form):   
        form.instance.author = self.request.user
        form.instance.neighborhood = self.request.user.profile.neighborhood
        return super().form_valid(form)

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.author:
            return True
        return False


class ContactDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    success_url = '/'

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.author:
            return True
        return False



class NeighborhoodCreateView(CreateView):
    model = Neighborhood
    fields = ['name', 'location', 'occupants_count', 'hood_image']

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

class NeighborhoodUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Neighborhood
    fields = ['name', 'location', 'occupants_count', 'hood_image']

    def form_valid(self, form):   
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def test_func(self):
        neighborhood = self.get_object()
        if self.request.user == neighborhood.admin:
            return True
        return False


class NeighborhoodDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Neighborhood
    success_url = '/'

    def test_func(self):
        neighborhood = self.get_object()
        if self.request.user == neighborhood.admin:
            return True
        return False