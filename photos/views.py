from django.shortcuts import render
from .models import Image,User,Category,Location
import datetime as dt
from django.http import Http404


def photos(request):
    photos=Image.objects.all()
    date=dt.date.today()
    users=User.objects.all()
    category=Category.objects.all()
    location=Location.objects.all()
    return render(request,'main/photos.html',{'photos':photos,'date':date,'category':category,'location':location})

def search(request):
    if 'Photo' in request.GET and request.GET['Photo']:
        search_term=request.GET.get('Photo')
        searched_photo=Category.search(search_term)
        message=f"{search_term}"
        
        return render(request,'main/search.html',{"message":message,"photos":searched_photo})
    else:
        message="You haven't searched for any term"
        return render(request,"main/search.html",{"message":message})
    
def single_photo(request,photo_id):
    try:
        photo=Image.objects.get(id=photo_id)
        photo_descriptions=Image.objects.get(id=photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'main/photo.html',{'photo':photo,"photo_descriptions":photo_descriptions})