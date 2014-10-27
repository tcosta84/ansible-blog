# -*- coding: utf-8 -*-

from django.conf import settings

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.cache import cache


from core import models


class ArticleListView(ListView):
    def get_queryset(self):
        if cache.get('article_list'):
            return cache.get('article_list')

        article_list = models.Article.objects.select_related('category').filter(
            status=models.Article.LIVE_STATUS,
            language=settings.LANGUAGE_CODE,
        ).order_by('-publish_date')

        cache.set('article_list', article_list)
        return article_list

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)

        if cache.get('blog'):
            blog = cache.get('blog')
        else:
            blog = models.Blog.objects.first()
            cache.set('blog', blog)

        context['blog'] = blog
        return context


class ArticleDetailView(DetailView):
    model = models.Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)

        if cache.get('blog'):
            blog = cache.get('blog')
        else:
            blog = models.Blog.objects.first()
            cache.set('blog', blog)

        context['blog'] = blog
        return context


class CategoryDetailView(DetailView):
    model = models.Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)

        if cache.get('blog'):
            blog = cache.get('blog')
        else:
            blog = models.Blog.objects.first()
            cache.set('blog', blog)

        context['blog'] = blog
        context['article_list'] = models.Article.objects.select_related('category').filter(
            status=models.Article.LIVE_STATUS,
            language=settings.LANGUAGE_CODE,
            category__slug=self.kwargs['slug']
        ).order_by('-publish_date')
        return context
