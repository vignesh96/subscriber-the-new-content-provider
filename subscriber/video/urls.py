from django.urls import path
from . import views
from .views import VideoListView, about, VideoUploadView

urlpatterns = [
    path('', VideoListView.as_view(), name='main-home'),
    path('video/new/', VideoUploadView.as_view(), name='video-upload'),
    path('about/', views.about, name='video-about')
   
]