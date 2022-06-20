# Generated by Django 4.0.5 on 2022-06-20 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('occupants_count', models.IntegerField()),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_hood.jpg', force_format=None, keep_meta=True, quality=75, size=[1000, 1000], upload_to='hood_images')),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('hood_image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_hood.jpg', force_format=None, keep_meta=True, quality=75, size=[1000, 1000], upload_to='hood_images')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]