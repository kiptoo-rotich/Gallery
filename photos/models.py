from django.db import models

class Image(models.Model):
    image=models.ImageField(upload_to='images/',default="Image")
    image_name=models.CharField(max_length=40)
    image_description=models.TextField(blank=False)
    
    def __str__(self):
        return self.image