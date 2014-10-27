# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.timezone import now


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    cover = models.ImageField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    @property
    def url(self):
        return reverse('blog:article-list')

    def __unicode__(self):
        return u'%s' % (self.title, )


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.name, )


class Article(models.Model):
    DRAFT_STATUS = 0
    LIVE_STATUS = 1

    STATUS_CHOICES = (
        (DRAFT_STATUS, u'Rascunho'),
        (LIVE_STATUS, u'No ar'),
    )

    language = models.CharField(max_length=10, choices=settings.LANGUAGES, 
        default=settings.LANGUAGE_CODE)
    author = models.ForeignKey('Author', related_name='articles')
    category = models.ForeignKey('Category', related_name='articles')
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    publish_date = models.DateTimeField(default=now)
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES,
        default=DRAFT_STATUS
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:article-detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return u'%s' % (self.slug, )


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:category-detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return u'%s' % (self.name, )


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.name, )
