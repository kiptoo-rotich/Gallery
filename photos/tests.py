from django.test import TestCase
from .models import User,Image
import datetime as dt

class UserTestClass(TestCase):
    #setup method
    def setUp(self):
        self.enock=User(firstname="Enock",lastname="Rotich",email="rotichenoch27@gmail.com",phone_number="1234567890")
    
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.enock,User))
        
    #Testing save method
    def test_save_method(self):
        self.enock.save_user()
        users=User.objects.all()
        self.assertTrue(len(users)>0)
        
    #Testing delete method
    def test_delete_method(self):
        self.enock.save_user()
        self.enock.delete_user()
        users=User.objects.all()
        self.assertTrue(len(users)==0)    
    

class ImageTestCase(TestCase):
    #setup method
    def setup(self):
        self.image=Image(image="media/images/Man.PNG",image_name="Man",image_description="This is an image of the man",user="Enock",category="Travel",location="Nairobi",pub_date=dt.today())
    
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
    