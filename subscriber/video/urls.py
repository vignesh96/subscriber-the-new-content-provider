from django.urls import path
from . import views
from .views import VideoListView

urlpatterns = [
    path('', VideoListView.as_view(), name='main-home')
]