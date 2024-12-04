from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student_page(request):
    return HttpResponse("<h1>Bu student sahifasi</h1>")