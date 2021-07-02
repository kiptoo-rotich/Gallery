from django.shortcuts import render

def photos(request):
    return render(request,'main/photos.html')
