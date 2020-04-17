from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from s3direct.fields import S3DirectField

# Create your models here.
class Upload(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    s3_url = models.CharField(max_length=100, blank=True)
    no_of_likes = models.IntegerField(default=0)
    content = models.TextField(default='')
    video = models.FileField(upload_to='videos')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
         return reverse('main-home')