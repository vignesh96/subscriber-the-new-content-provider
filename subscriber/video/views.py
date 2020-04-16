from django.shortcuts import render, get_object_or_404
from .models import Upload
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


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
    fields = ['title', 'content', 'genre']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)