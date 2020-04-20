from django.shortcuts import render, get_object_or_404, reverse
from .models import Upload, Poll
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView, FormView
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.db.models import Max, F
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.conf import settings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Upload
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

class ShareVideoView(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk=None, format=None):
        
        obj = get_object_or_404(Upload, pk=pk)
        url = obj.get_absolute_url() + "video/{}".format(pk)
        user = self.request.user
        subject = "Meteor Entertainment video shared by {}".format(user)
        print(url)
        body = """<p>Hi User,</p>
        <p>Greetings from Meteor Entertainment!</p>
        <p> A video has been shared by user {0}
         on behalf of Meteor Entertainment. The link to the video is <a href="{1}">{1}</a>.</p>
        <p>Create your own MeteorLive account to watch this video and more amazing videos of your choice.</p>
        <br>
        <p>Regards,<br>Team Meteor Entertainment</p>""".format(user, url)
        from_mail = settings.EMAIL_HOST_USER
        print(request)
        to_mail = request.POST.get("email")
        
        # Setup SMTP connection
        s = smtplib.SMTP(host=settings.EMAIL_HOST, port=settings.EMAIL_PORT)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(from_mail, settings.EMAIL_HOST_PASSWORD)
        msg = MIMEMultipart()
        msg['From'] = from_mail
        msg['To'] = to_mail
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))
        s.send_message(msg)
        del msg

        # Terminate the SMTP session and close the connection
        s.quit()
        return HttpResponseRedirect(reverse('main-home'))

def VideoPollView(request):
    context = {
        'polls': Poll.objects.all()
    }
    return render(request, 'video/upload_poll.html', context=context)
