from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):
    excerpt = forms.CharField(widget=forms.Textarea(
        attrs={
            'rows': 3,
            'placeholder': ('Enter a short description about the post'
                            ' to be shown on post list page')
        }))

    class Meta:
        model = Post
        exclude = ("slug",)
