from django.shortcuts import render, get_object_or_404
from .models import Upload
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.db.models import Max, F
def home(request):
    context = {
        'uploads': Upload.objects.all()
    }
    return render(request, 'video/home.html', context=context)

# Create your views here.
class VideoListView(ListView):
    model = Upload
    template_name = "video/home.html"
    context_object_name = 'uploads'
    ordering = ['-date_posted']
    paginate_by = 5

def about(request):
    return render(request, 'video/about.html', context={'title':'About'})

class VideoUploadView(LoginRequiredMixin, CreateView):
    model = Upload
    fields = ['title', 'content', 'genre', 'video']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class VideoDetailView(DetailView):
    model = Upload

    def get_object(self, queryset=None):
        item = super().get_object(queryset)
        item.incrementViewCount()
        return item

class VideoLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk=None, format=None):
        if request.is_ajax():
            obj = get_object_or_404(Upload, pk=pk)
            url_ = obj.get_absolute_url() + "video/{}".format(id)
            user = self.request.user
            updated = False
            liked = False
            disliked = True
            if user.is_authenticated:
                if user in obj.likes.all():
                    liked = False
                    obj.likes.remove(user)
                    
                else:
                    liked = True
                    obj.likes.add(user)
                    
                    if user in obj.dislikes.all():
                        obj.dislikes.remove(user)
                        disliked = False
                updated = True
            data = {
                "updated": updated,
                "liked": liked,
                "disliked": disliked
            }
        return Response(data)

class VideoUnLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk=None, format=None):
        if request.is_ajax():
            obj = get_object_or_404(Upload, pk=pk)
            url_ = obj.get_absolute_url() + "video/{}".format(id)
            user = self.request.user
            updated = False
            liked = True
            disliked = False
            if user.is_authenticated:
                if user in obj.dislikes.all():
                    obj.dislikes.remove(user)
                    disliked = False
                else:
                    obj.dislikes.add(user)
                    disliked = True
                    if user in obj.likes.all():
                        obj.likes.remove(user)
                        liked = False
                updated = True
            data = {
                "updated": updated,
                "liked": liked,
                "disliked": disliked
            }
        return Response(data)

class UserVideoListView(ListView):
    model = Upload
    template_name = "video/upload_user.html"
    context_object_name = 'uploads'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Upload.objects.filter(author=user).order_by('-date_posted')

class PopularVideoListView(ListView):
    model = Upload
    template_name = "video/upload_popular.html"
    context_object_name = 'uploads'
    paginate_by = 5

    def get_queryset(self):
        return Upload.objects.annotate(max_weight=Max(F('likes') - F('dislikes'))).order_by('-max_weight')

class MostViewedVideoListView(ListView):
    model = Upload
    template_name = "video/upload_viewed.html"
    context_object_name = 'uploads'
    paginate_by = 5

    def get_queryset(self):
        return Upload.objects.order_by('-views')

