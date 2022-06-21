from django.db import models
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

class Neighborhood(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    location = models.CharField(null=True, blank=True, max_length=200)
    occupants_count = models.IntegerField()

    #Image
    hood_image = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_hood.jpg', upload_to='hood_images')

    # Related Field
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    # Utility Variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
 
   
    def __str__(self):
        return '{} {}'.format(self.name, self.uniqueId)

    
    def get_absolute_url(self):
        return reverse('neighborhoods')

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.name, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.name, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Neighborhood, self).save(*args, **kwargs)



class Business(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    email_address = models.EmailField()

    # Related Fields
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, blank=True)
    business_image = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_business.jpg', upload_to='business_images')

    # Utility Variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
 
   
    def __str__(self):
        return '{} {}'.format(self.name, self.uniqueId)

    
    def get_absolute_url(self):
        return reverse('business')

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.name, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.name, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Business, self).save(*args, **kwargs)


    @classmethod
    def search_by_name(cls,search_term):
        businesses = cls.objects.filter(name__icontains=search_term)

        return businesses



class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, blank=True)

    post_image = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_post.jpg', upload_to='posts')

    # Utility Variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
 
   
    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Post, self).save(*args, **kwargs)



class Contact(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    phone_number = models.CharField(null=True, blank=True, max_length=200)
    email_address = models.EmailField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, blank=True)


    # Utility Variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
 
   
    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    
    def get_absolute_url(self):
        return reverse('contacts')

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Contact, self).save(*args, **kwargs)

