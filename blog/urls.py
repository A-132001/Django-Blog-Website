from django.urls import path
from .views import (
PostListViews,
PostDetailsViews,
PostCreateViews,
PostUpdateViews,
PostDeleteViews,
UserPostListViews,

)
from . import views
urlpatterns = [
    path('', PostListViews.as_view(),name = 'blog-home'),
    path('user/<str:username>', UserPostListViews.as_view(),name = 'user-posts'),
    path('post/<int:pk>/', PostDetailsViews.as_view(),name = 'post-details'),
    path('post/new/', PostCreateViews.as_view(),name = 'post-create'),
    path('post/<int:pk>/update', PostUpdateViews.as_view(),name = 'post-update'),
    path('post/<int:pk>/delete', PostDeleteViews.as_view(),name = 'post-delete'),
    path('about/', views.about,name = 'blog-about'),
    ]