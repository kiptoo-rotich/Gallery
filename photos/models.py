from django.db import models
import datetime as dt
class User(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    phone_number=models.CharField(max_length=10,blank=True)
    
    def __str__(self):
        return self.firstname
    
    def save_user(self):
        self.save()
    
    def delete_user(self):
        self.delete()
    
    def update_user(self):
        self.update(firstname)

class Image(models.Model):
    image=models.ImageField(upload_to='images/',default="Image")
    image_name=models.CharField(max_length=40)
    image_description=models.TextField(blank=False,default="Image description")
    user = models.ForeignKey('User',on_delete=models.CASCADE,)
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def update_image(self):
        self.update(image)
    
    @classmethod
    def get_image_by_id(cls,id):
        image=cls.objects.get(id=id)
        return image
        
    @classmethod
    def search(cls,search_term):
        photos=cls.objects.filter(title__icontains=search_term)
        return photos
        
class Category(models.Model):
    category=models.CharField(max_length=30)
    image = models.ManyToManyField('Image')
    user = models.ForeignKey('User',on_delete=models.CASCADE)

    
    def __str__(self):
        return self.category
    
    @classmethod
    def search(cls,search_term):
        photos=cls.objects.filter(category__icontains=search_term)
        return photos
    
class Location(models.Model):
    location=models.CharField(max_length=30)
    user = models.ForeignKey('User',on_delete=models.CASCADE,)

    def __str__(self):
        return self.location