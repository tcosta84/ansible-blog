# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from blog import models


class TestArticleListView(TestCase):
    def test_get(self):
        blog = models.Blog.objects.create(title='Blog title', description='Blog description')

        response = self.client.get(reverse('blog:article-list'))

        self.assertEqual(200, response.status_code)
        self.assertEqual('Blog title', response.context['meta_title'])
        self.assertEqual('Blog description', response.context['meta_description'])
        self.assertEqual(blog, response.context['blog'])


class TestArticleDetailView(TestCase):
    def test_get(self):
        blog = models.Blog.objects.create(title='Title', description='Description')
        author = models.Author.objects.create(name='Author name', bio='Author bio')
        category = models.Category.objects.create(name='Category name', slug='category-name')
        models.Article.objects.create(author=author, category=category, 
                title='Article title', slug='article-slug', )

        response = self.client.get(reverse('blog:article-detail', kwargs={'slug': 'article-slug'}))

        self.assertEqual(200, response.status_code)
        self.assertEqual('Article title', response.context['meta_title'])
        self.assertEqual('', response.context['meta_description'])
        self.assertEqual(blog, response.context['blog'])


class TestCategoryDetailView(TestCase):
    def test_get(self):
        blog = models.Blog.objects.create(title='Blog title', description='Blog description')
        author = models.Author.objects.create(name='Author name', bio='Author bio')
        category = models.Category.objects.create(name='Category name', slug='category-slug')
        models.Article.objects.create(author=author, category=category, 
                title='Article title', slug='article-title', )

        response = self.client.get(reverse('blog:category-detail', kwargs={'slug': 'category-slug'}))

        self.assertEqual(200, response.status_code)
        self.assertEqual('Blog title', response.context['meta_title'])
        self.assertEqual('Blog description', response.context['meta_description'])
        self.assertEqual(blog, response.context['blog'])
