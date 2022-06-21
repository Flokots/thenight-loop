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

def search_results(request):
    if 'business' in request.GET and request.GET['business']:
        search_term = request.GET.get('business')
        searched_businesses = Business.search_by_name(search_term)

        message = f'{search_term}'

        return render(request, 'search.html', {'message': message, 'businesses': searched_businesses})

    else:
        message = "You haven't searched for any business"
        return render(request, 'search.html', {'message': message})


def search_hood_results(request):
    if 'hood' in request.GET and request.GET['hood']:
        search_term = request.GET.get('hood')
        searched_hoods = Neighborhood.search_hood_by_name(search_term)

        message = f'{search_term}'

        return render(request, 'search_hood.html', {'message': message, 'hoods': searched_hoods})

    else:
        message = "You haven't searched for any hood"
        return render(request, 'search_hood.html', {'message': message})



class PostListView(ListView):
    model = Post
    template_name = 'index.html' # Expected </app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.neighborhood = self.request.user.profile.neighborhood
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
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




class BusinessListView(LoginRequiredMixin,  ListView):
    model = Business
    template_name = 'business.html' # Expected </app>/<model>_<viewtype>.html
    context_object_name = 'businesses'
    ordering = ['-date_created']
    paginate_by = 3


class BusinessCreateView(LoginRequiredMixin, CreateView):
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
    success_url = '/business/'

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.owner:
            return True
        return False



class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contact.html' # Expected </app>/<model>_<viewtype>.html
    context_object_name = 'contacts'
    ordering = ['-date_posted']
    paginate_by = 3


class ContactCreateView(LoginRequiredMixin, CreateView):
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
    success_url = '/contacts/'

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.author:
            return True
        return False



class NeighborhoodListView(LoginRequiredMixin, ListView):
    model = Neighborhood
    template_name = 'neighborhood.html' # Expected </app>/<model>_<viewtype>.html
    context_object_name = 'neighborhoods'
    ordering = ['-date_created']
    paginate_by = 3


class NeighborhoodCreateView(LoginRequiredMixin, CreateView):
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
    success_url = '/neighborhoods/'

    def test_func(self):
        neighborhood = self.get_object()
        if self.request.user == neighborhood.admin:
            return True
        return False