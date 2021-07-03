from django.test import TestCase
from .models import User,Image

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
    
    #Testing update method
    def test_update_method2(self,firstname):
        self.enock.save_user()
        editted = User.objects.get(firstname="Enock").update(firstname="Kiptoo")
        self.assertEqual(first, second)(User.objects.get(lastname="Rotich"), User.objects.get(firstname="Kiptoo"))