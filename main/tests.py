from django.test import TestCase
from django.contrib.auth.models import User
from .models import Neighborhood

# Create your tests here.

class NeighborhoodTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.new_user = User(id=1, username='new_user')
        self.new_hood = Neighborhood(id=1, name='Test Hood', location='Test Location', occupants_count='15', hood_image='../media/default_hood.jpg', admin=self.new_user)

    def tearDown(self):
        User.objects.all().delete()
        Neighborhood.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_hood, Neighborhood))

    # Testing save method
    def test_save(self):
        self.new_hood.save()
        hoods= Neighborhood.objects.all()
        self.assertTrue(len(hoods) > 0)

    
    def test_delete(self):
        self.new_hood.delete()
        hoods= Neighborhood.objects.all()
        self.assertTrue(len(hoods) == 0)
    

    def test_update(self):
        self.new_hood.name= 'New Hood'
        self.new_hood.save()
        self.assertEqual(self.new_hood.name, 'New Hood')

    
    def test_search_hood_by_name(self):
        self.hood= Neighborhood.search_hood_by_name('Test Hood')

        self.assertEqual(self.new_hood.name ,'Test Hood')