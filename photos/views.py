from django.shortcuts import render
from .models import Image

def photos(request):
    photos=Image.objects.all()
    return render(request,'main/photos.html',{'photos':photos})
