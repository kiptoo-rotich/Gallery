from django.shortcuts import render
from .models import Image,User
import datetime as dt


def photos(request):
    photos=Image.objects.all()
    date=dt.date.today()
    users=User.objects.all()
    return render(request,'main/photos.html',{'photos':photos,'date':date})
