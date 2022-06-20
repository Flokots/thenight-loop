from django.contrib import admin
from .models import Neighborhood, Business, Post, Contact

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Contact)