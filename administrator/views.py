from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def admin_page(request):
    text = """<h1>Bu administrator sahifasi</h1><h2>bu bosh sahifa</h2>"""
    return HttpResponse(text)
