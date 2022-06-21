from django.test import TestCase
from django.contrib.auth.models import User
from .models import Neighborhood, Business, Post, Contact

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



class BusinessTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.new_user = User(id=1, username='new_user')
        self.new_hood = Neighborhood(id=1, name='Test Hood', location='Test Location', occupants_count='15', hood_image='../media/default_hood.jpg', admin=self.new_user)
        self.new_business = Business(id=1, name='New Business', email_address='email@gmail.com', owner=self.new_user, neighborhood=self.new_hood, business_image='../media/default_business.jpg')

    def tearDown(self):
        User.objects.all().delete()
        Neighborhood.objects.all().delete()
        Business.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_business, Business))

    # Testing save method
    def test_save(self):
        self.new_business.save()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    
    def test_delete(self):
        self.new_business.delete()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)
    

    def test_update(self):
        self.new_business.name= 'Test Business'
        self.new_business.save()
        self.assertEqual(self.new_business.name, 'Test Business')

    
    def test_search_by_name(self):
        self.business= Business.search_by_name('New Business')

        self.assertEqual(self.new_business.name ,'New Business')



class PostTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.new_user = User(id=1, username='new_user')
        self.new_hood = Neighborhood(id=1, name='Test Hood', location='Test Location', occupants_count='15', hood_image='../media/default_hood.jpg', admin=self.new_user)
        self.new_post = Post(id=1, title='New Post', description='New Description', author=self.new_user, neighborhood=self.new_hood, post_image='../media/default_post.jpg')

    def tearDown(self):
        User.objects.all().delete()
        Neighborhood.objects.all().delete()
        Post.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    # Testing save method
    def test_save(self):
        self.new_post.save()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    
    def test_delete(self):
        self.new_post.delete()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 0)
    

    def test_update(self):
        self.new_post.title= 'Test Post'
        self.new_post.save()
        self.assertEqual(self.new_post.title, 'Test Post')

 
class ContactTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.new_user = User(id=1, username='new_user')
        self.new_hood = Neighborhood(id=1, name='Test Hood', location='Test Location', occupants_count='15', hood_image='../media/default_hood.jpg', admin=self.new_user)
        self.new_contact = Contact(id=1, title='New Contact', description='New Description', phone_number='0712345678', email_address='test@gmail.com', author=self.new_user, neighborhood=self.new_hood)

    def tearDown(self):
        User.objects.all().delete()
        Neighborhood.objects.all().delete()
        Contact.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_contact, Contact))

    # Testing save method
    def test_save(self):
        self.new_contact.save()
        contacts = Contact.objects.all()
        self.assertTrue(len(contacts) > 0)

    
    def test_delete(self):
        self.new_contact.delete()
        contacts = Contact.objects.all()
        self.assertTrue(len(contacts) == 0)
    

    def test_update(self):
        self.new_contact.title= 'Test Contact'
        self.new_contact.save()
        self.assertEqual(self.new_contact.title, 'Test Contact')

 
