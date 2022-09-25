from typing import List
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,)
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


def home(request):
    context = {
        'postes':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListViews(ListView):
    model= Post
    template_name = 'blog/home.html'
    context_object_name= 'postes'
    ordering = ['-posted_date']
    paginate_by = 4

class UserPostListViews(ListView):
    model= Post
    template_name = 'blog/user_posts.html'
    context_object_name= 'postes'
    paginate_by = 4
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-posted_date')

class PostDetailsViews(DetailView):
    model= Post
    template_name = 'blog/details.html'

class PostCreateViews(LoginRequiredMixin,CreateView):
    model= Post
    template_name = 'blog/new_post.html'
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateViews(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model= Post
    template_name = 'blog/new_post.html'
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteViews(DeleteView):
    model= Post
    template_name = 'blog/delete_confirm.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request,'blog/about.html',{'title':'About'})
