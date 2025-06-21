from django.contrib.auth import get_user_model
from django.db import models
from django import forms
from django.urls import reverse
from ckeditor.fields import RichTextField

# # Create your models here.
class Post(models.Model):
        title = models.CharField(max_length=200)
        summary = models.CharField(max_length=250, blank=True)
        body = RichTextField()
        photo = models.CharField(max_length=255))
        date = models.DateField(auto_now_add=True)
        author = models.ForeignKey(
            get_user_model(),
            on_delete=models.CASCADE
        )
        # img = models.ImageField()
        def __str__(self):
            return self.title

        def get_absolute_url(self):
            return reverse('post_detail', args=[str(self.id)])

class Comments(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    comment = RichTextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('comment_detail', args=[str(self.id)])
