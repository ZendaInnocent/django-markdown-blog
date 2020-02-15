from django.test import TestCase

from posts.models import Post, Tag


class PostModelTest(TestCase):

    def test_saving_and_retrieving_posts(self):
        first_post = Post.objects.create(title='Post 1', content='The post detail')
        second_post = Post.objects.create(title='Post 2', content='The post detail')

        saved_posts = Post.objects.all()

        self.assertEqual(saved_posts.count(), 2)

        first_saved_post = Post.objects.all()[0]
        second_saved_post = Post.objects.all()[1]

        self.assertIn(first_saved_post.title, 'Post 1')
        self.assertIn(second_saved_post.title, 'Post 2')


    def test_saving_retrieving_tags(self):
        tag1 = Tag.objects.create(name='first tag')
        tag2 = Tag.objects.create(name='second tag')

        saved_tags = Tag.objects.all()

        self.assertEqual(saved_tags.count(), 2)

        saved_tag1 = Tag.objects.all()[0]
        saved_tag2 = Tag.objects.all()[1]

        self.assertIn(saved_tag1.name, 'first tag')
        self.assertIn(saved_tag2.name, 'second tag')


    def test_string_representation_for_post(self):
        post = Post.objects.create(title='The first post', content='The post detail')
        self.assertEqual(str(post), post.title)


    def test_string_representation_for_tag(self):
        tag = Tag.objects.create(name='Django')
        self.assertEqual(str(tag), tag.name)