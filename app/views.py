from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Comment, Category

# Create your views here.
def home(request):
    # Tüm ** yayınlanmış ** postları veritabanından çek(published=True olanlar)
    # - Tüm kategorileri çek - Bunları context dictionary 'sine ekle - Template 'e gönder
    posts = Post.objects.filter(published = True)
    categories = Category.objects.all()
    context = {
        'categories' : categories,
        'posts' : posts,

    }
    return render(request, 'app/home.html', context)

def posts(request):
    return HttpResponse('Posts Page')

def post(request, slug):
    return HttpResponse('Post Page')

def category(request, id):
    return HttpResponse("Category Page")

def profile(request):
    return HttpResponse('Profile Page')