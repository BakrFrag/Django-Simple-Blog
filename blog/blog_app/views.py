from django.shortcuts import render,get_object_or_404;
from .models import Post;
from django.contrib import messages;
# from django.contrib.messages.views import SuccessMessageMixin;
# from django.urls import reverse;
from django.views.generic import (ListView,
DetailView,CreateView,UpdateView,DeleteView);
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin;
from django.contrib.auth.models import User;
# from django.core.paginator import Paginator;
# Create your views here
#views => DetailView ListView CreteView DeleteView FormView RedirectView MxinView
#<app_name>/<mode_name>_<view_type.html>
#default context_object_name=object_list ListView
#detailView object
def home(request):
    posts=Post.objects.all();
    context={
        "posts":posts
    };
    return render(request,"blog_app/home.html",context);
def about(request):
    return render(request,"blog_app/about.html");
class PostListView(ListView):
    model=Post;
    context_object_name="posts";
    template_name="blog_app/home.html";
    ordering=['-date'];
    paginate_by=2;
class UserPostListView(ListView):
        model=Post;
        context_object_name="posts";
        template_name="blog_app/user.html";

        paginate_by=2;
        def get_queryset(self):
            user=get_object_or_404(User,username=self.kwargs.get('username'));
            return Post.objects.filter(author=user).order_by('-date');
    #paginate_to;
class PostDetailView(DetailView):
    model=Post;
    context_object_name="post";
    template_name="blog_app/post.html";
class PostCreateView(CreateView):
    model=Post;
    template_name="blog_app/create_post.html"
    fields=['title','content'];
    def form_valid(self,form):
        form.instance.author=self.request.user;
        return super().form_valid(form);
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post;
    fields=['title','content'];
    template_name="blog_app/create_post.html";
    def form_valid(self,form):
        form.instance.author=self.request.user;
        return super().form_valid(form);
    def test_func(self):
        post=self.get_object();
        if self.request.user==post.author:
            return True;
        return False;
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post;
    success_url="/";
    def test_func(self):
        post=self.get_object();
        if self.request.user==post.author:
            return True;
        return False;
