from django.urls import path
from . import views
from .views import VideoListView, about, VideoUploadView, VideoDetailView, VideoLikeAPIToggle, VideoUnLikeAPIToggle

urlpatterns = [
    path('', VideoListView.as_view(), name='main-home'),
    path('video/new/', VideoUploadView.as_view(), name='video-upload'),
    path('about/', views.about, name='video-about'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('video/<int:pk>/like', VideoLikeAPIToggle.as_view(), name='video-like-toggle'),
    path('video/<int:pk>/unlike', VideoUnLikeAPIToggle.as_view(), name='video-unlike-toggle'),
    
]