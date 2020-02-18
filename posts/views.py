from django.shortcuts import render, get_list_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from posts.models import Post, Tag
from posts.forms import PostCreateForm


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_object_name = 'post'
    template_name = 'posts/post_detail.html'


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = PostCreateForm
    template_name = 'posts/post_form.html'

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/post_update.html'
    success_message = 'Post updated successful.'

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = '/'
    success_message = 'Post deleted successful.'

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return True
        return False


class TagDetailView(DetailView):
    model = Tag
    template_name = 'posts/post_tag_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = Tag.objects.get(slug=self.kwargs['slug'])
        context['object_list'] = tag.post_set.all()
        return context

def content_view(request):
    return render(request, 'posts/test.html', {'content':
        '# this is test title\n' + 
        '- list 1\n' +
        '- list 2\n'
    })