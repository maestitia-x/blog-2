from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('Home Page')

def posts(request):
    return HttpResponse('Posts Page')

def post(request, slug):
    return HttpResponse('Post Page')

def category(request, id):
    return HttpResponse("Category Page")

def profile(request):
    return HttpResponse('Profile Page')