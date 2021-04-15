from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http.response import HttpResponseBadRequest
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from posts.forms import PostCreateForm
from posts.models import Post, Tag


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_object_name = 'post'
    template_name = 'posts/post_detail.html'


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin,
                     SuccessMessageMixin, CreateView):
    form_class = PostCreateForm
    success_message = 'Post created successful'
    extra_context = {
        'title': 'Create Post'
    }

    def form_valid(self, form):
        action = self.request.POST.get('action')
        if action == 'SAVE':
            return super().form_valid(form)
        elif action == 'PREVIEW':
            preview = Post(
                title=form.cleaned_data['title'],
                excerpt=form.cleaned_data['excerpt'],
                content=form.cleaned_data['content'],
                # tags=form.cleaned_data['tags'],
            )
            context = self.get_context_data(preview=preview)
            return self.render_to_response(context=context)

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                     SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostCreateForm
    success_message = 'Post updated successful.'
    extra_context = {
        'title': 'Update Post'
    }

    def form_valid(self, form):
        action = self.request.POST.get('action')
        if action == 'SAVE':
            return super().form_valid(form)
        elif action == 'PREVIEW':
            preview = Post(
                title=form.cleaned_data['title'],
                excerpt=form.cleaned_data['excerpt'],
                content=form.cleaned_data['content'],
                # tags=form.cleaned_data['tags'],
            )
            context = self.get_context_data(preview=preview)
            return self.render_to_response(context=context)

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                     SuccessMessageMixin, DeleteView):
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
    template_name = 'posts/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = Tag.objects.get(slug=self.kwargs['slug'])
        context['object_list'] = tag.post_set.all()
        return context
