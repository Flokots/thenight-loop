from email.policy import default
from msilib.schema import ReserveCost
from django.db import models
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User


class Neighborhood(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    location = models.CharField(null=True, blank=True, max_length=200)
    occupants_count = models.IntegerField()

    #Image
    image = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_hood.jpg', upload_to='hood_images')
    
    # Related Field
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    # Utility Variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
 
    #Image
    hood_image = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_hood.jpg', upload_to='hood_images')

    def __str__(self):
        return '{} {}'.format(self.name, self.uniqueId)

    
    def get_absolute_url(self):
        return reverse('neighborhood-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.name, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.name, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Neighborhood, self).save(*args, **kwargs)

