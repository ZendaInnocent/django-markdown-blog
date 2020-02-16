from django.shortcuts import render, get_list_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from posts.models import Post, Tag
from posts.forms import PostCreateForm


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_object_name = 'post'
    template_name = 'posts/post_detail.html'


class PostCreateView(CreateView):
    form_class = PostCreateForm
    template_name = 'posts/post_form.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/post_update.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = '/'


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