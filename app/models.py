
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, SET_NULL
from django.template.defaultfilters import title


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Categories'
#
# Model 2: Post (Blog Yazısı)
# Alanlar:
#
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=CASCADE, related_name='blog_posts')
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True)
    category = models.ForeignKey(Category,null=True, on_delete=SET_NULL, related_name='posts')
    image = models.ImageField(blank=True, upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    published = models.BooleanField(default=False)
    views = models.IntegerField(default=0, null=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author.username} - {self.post.title}"

    class Meta:
        ordering = ['-created_at']
