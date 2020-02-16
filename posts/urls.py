from django.urls import path

from posts import views


app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('md/', views.content_view, name='test'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('tag/<slug:slug>/', views.TagDetailView.as_view(), name='tag-detail'),
]