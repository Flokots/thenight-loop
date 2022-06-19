from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

# Create your tests here.

class ProfileTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.new_user = User(id=1, username='new_user')
        self.new_profile = Profile(id=1, bio='Test Bio', image='../media/default_user.jpg', user=self.new_user)

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    # Testing save method
    def test_save(self):
        self.new_profile.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    
    def test_delete(self):
        self.new_profile.delete()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)
    

    def test_update(self):
        self.new_profile.bio = 'New Bio'
        self.new_profile.save()
        self.assertEqual(self.new_profile.bio, 'New Bio')
