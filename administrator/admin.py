from django.contrib import admin
from .models import Students, Teachers
from django.conf import settings
from django.conf.urls.static import static

admin.site.register(Students)
admin.site.register(Teachers)