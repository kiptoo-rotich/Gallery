from django.shortcuts import render
from .models import Image,User
import datetime as dt


def photos(request):
    photos=Image.objects.all()
    date=dt.date.today()
    users=User.objects.all()
    return render(request,'main/photos.html',{'photos':photos,'date':date})

def search(request):
    if 'photo' in request.GET and request.GET['photo']:
        search_term=request.GET('photo')
        searched_photo=Image.search(search_term)
        message=f"{search_term}"
        
        return render(request,'main/search.html',{"message":message,"photos":searched_photo})
    else:
        message="You haven't searched for any term"
        return render(request,"main/search.html",{"message":message})