from django.test import SimpleTestCase
from django.urls import resolve, reverse
from posts import views


class TestPostsUrls(SimpleTestCase):

    def test_post_list_url_resolves(self):
        list_url = reverse('posts:post-list')

        self.assertEqual(resolve(list_url).func.view_class, views.PostListView)

    def test_post_detail_url_resolves(self):
        detail_url = reverse('posts:post-detail', kwargs={'slug': 'some-slug'})

        self.assertEqual(resolve(detail_url).func.view_class,
                         views.PostDetailView)

    def test_post_create_url_resolves(self):
        create_url = reverse('posts:post-create')

        self.assertEqual(resolve(create_url).func.view_class,
                         views.PostCreateView)

    def test_post_update_url_resolves(self):
        update_url = reverse('posts:post-update', kwargs={'slug': 'some-slug'})

        self.assertEqual(resolve(update_url).func.view_class,
                         views.PostUpdateView)

    def test_post_delete_url_resolves(self):
        delete_url = reverse('posts:post-delete', kwargs={'slug': 'some-slug'})

        self.assertEqual(resolve(delete_url).func.view_class,
                         views.PostDeleteView)

    def test_tag_detail_url_resolves(self):
        tag_detail_url = reverse(
            'posts:tag-detail', kwargs={'slug': 'some-slug'})

        self.assertEqual(
            resolve(tag_detail_url).func.view_class, views.TagDetailView)
