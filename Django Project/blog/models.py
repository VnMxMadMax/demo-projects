from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
    
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name