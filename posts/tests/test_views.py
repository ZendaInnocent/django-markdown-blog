from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from posts import views
from posts.models import Post, Tag


class PostsViewsTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='First Post',
            thumbnail='assets/banner/hero-image.svg',
        )
        self.staff_user = User.objects.create_user(
            username='Inno', password='adfshou94y840', is_staff=True)
        self.user = User.objects.create_user(
            username='user', password='foiafdyohfads', is_staff=False)

    def test_root_url_resolve_to_home_page(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_home_page_returns_list_of_all_posts(self):
        response = self.client.get(reverse('posts:post-list'))

        self.assertEqual(response.status_code, 200)
        # to-do

    def test_post_detail_view_uses_post_detail_template(self):
        response = self.client.get(reverse('posts:post-detail',
                                           kwargs={'slug': self.post.slug}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_detail.html')

    def test_post_crate_view_use_post_form_template(self):
        self.client.login(username='Inno', password='adfshou94y840')
        response = self.client.get(reverse('posts:post-create'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_form.html')

    def test_post_create_view_redirect_with_anonymous_user(self):
        response = self.client.get(reverse('posts:post-create'))

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/post/create/')

    def test_post_update_view_redirect_with_anonymous_user(self):
        response = self.client.get(reverse('posts:post-update',
                                           kwargs={'slug': self.post.slug}))

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=/post/first-post/update/')

    def test_post_create_view_with_a_staff_user(self):
        self.client.login(username='Inno', password='adfshou94y840')
        response = self.client.get(reverse('posts:post-create'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_form.html')

    def test_post_update_view_with_a_staff_user(self):
        self.client.login(username='Inno', password='adfshou94y840')
        response = self.client.get(reverse('posts:post-update',
                                           kwargs={'slug': self.post.slug}))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_form.html')

    def test_post_delete_view_with_a_staff_user(self):
        self.client.login(username='Inno', password='adfshou94y840')
        response = self.client.get(reverse('posts:post-delete',
                                           kwargs={'slug': self.post.slug}))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_delete.html')

    def test_post_create_view_with_non_staff_user(self):
        self.client.login(username='user', password='foiafdyohfads')
        response = self.client.get(reverse('posts:post-create'))

        self.assertEquals(response.status_code, 403)

    def test_post_update_view_with_non_staff_user(self):
        self.client.login(username='user', password='foiafdyohfads')
        response = self.client.get(
            reverse('posts:post-update', kwargs={'slug': 'some-slug'}))

        self.assertEquals(response.status_code, 403)

    def test_post_delete_view_with_non_staff_user(self):
        self.client.login(username='user', password='foiafdyohfads')
        response = self.client.get(
            reverse('posts:post-delete', kwargs={'slug': self.post.slug}))

        self.assertEquals(response.status_code, 403)

    def test_tag_detail_view_uses_post_list_template(self):
        tag = Tag.objects.create(name='Python')
        response = self.client.get(
            reverse('posts:tag-detail', kwargs={'slug': tag.slug}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_list.html')

    def test_form_valid_method(self):
        """Test for `form_valid` method in `CreateUpdateMixin`"""
        request = RequestFactory().post('/post/create', {
            'title': 'sample post title',
            'excerpt': 'some exceodfo',
            'content': 'here goes the contents',
            'action': 'PREVIEW',
        })
        request.user = self.staff_user
        response = views.PostCreateView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        # todo: add more assertions
