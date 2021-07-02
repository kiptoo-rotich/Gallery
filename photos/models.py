from django.db import models

class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    image_name=models.CharField(max_length=40)
    image_description=models.TextField(blank=False)
    