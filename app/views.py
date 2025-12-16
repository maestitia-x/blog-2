from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
    #
    # URL'den gelen slug parametresini kullanarak ilgili postu bul Eğer post bulunamazsa 404 hatası döndür
    # Her ziyarette views sayısını 1 artır ve kaydet
    # Post 'un aktif yorumlarını çek (active=True) Bunları context 'e ekle ve template' e gönder
    post_obj = get_object_or_404(Post)
    post_obj.views += 1
    comments = post_obj.comments.filter(active=True)
    context={
        'post':post_obj,
        'comments':comments,
    }
    return render(request, 'app/post.html', context)

def category(request, id):
    return HttpResponse("Category Page")

def profile(request):
    return HttpResponse('Profile Page')