from django.urls import path
from . import views
from .views import (VideoListView, about, VideoUploadView, VideoDetailView, 
VideoLikeAPIToggle, VideoUnLikeAPIToggle, UserVideoListView, PopularVideoListView, MostViewedVideoListView,
VideoDeleteView, ShareVideoView, VideoPollView)

urlpatterns = [
    path('', VideoListView.as_view(), name='main-home'),
    path('video/new/', VideoUploadView.as_view(), name='video-upload'),
    path('about/', views.about, name='video-about'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('video/<int:pk>/like', VideoLikeAPIToggle.as_view(), name='video-like-toggle'),
    path('video/<int:pk>/unlike', VideoUnLikeAPIToggle.as_view(), name='video-unlike-toggle'),
    path('user/<str:username>', UserVideoListView.as_view(), name='user-videos'),
    path('video/popular', PopularVideoListView.as_view(), name='popular-videos'),
    path('video/most-viewed', MostViewedVideoListView.as_view(), name='most-viewed-videos'),
    path('video/<int:pk>/delete', VideoDeleteView.as_view(), name='video-delete'),
    path('video/<int:pk>/share', ShareVideoView.as_view(), name='share-video'),
    path('video/poll', views.VideoPollView, name='poll-video'),
    
]