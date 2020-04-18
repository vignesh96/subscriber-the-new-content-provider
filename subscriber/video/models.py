from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .validators import validate_file_size
from django.conf import settings
# Create your models here.
class Upload(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    s3_url = models.CharField(max_length=100, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='video_likes')
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='video_dislikes')
    content = models.TextField(default='')
    video = models.FileField(upload_to='videos', null=True, validators=[validate_file_size])
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
         return reverse('main-home')

    def get_like_url(self):
        return reverse('video-like-toggle', kwargs={"pk": self.pk})
    
    def get_unlike_url(self):
        return reverse('video-unlike-toggle', kwargs={"pk": self.pk})
    
    def incrementViewCount(self):
        self.views += 1
        self.save()
