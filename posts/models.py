from comment.models import Comment
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from mdeditor.fields import MDTextField


class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=100)
    content = MDTextField()
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True,
                                  null=True)
    tags = models.ManyToManyField(Tag)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    prev_post = models.ForeignKey(
        'self', related_name='previous_post', on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name='Previous Post')
    nxt_post = models.ForeignKey(
        'self', related_name='next_post', on_delete=models.SET_NULL, null=True,
        blank=True, verbose_name='Next Post')
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('posts:post-update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('posts:post-delete', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
