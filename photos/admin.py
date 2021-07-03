from django.contrib import admin
from .models import Image,User,Location,Category

admin.site.register(Image)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Location)