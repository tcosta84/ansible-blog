# -*- coding: utf-8 -*-

from django.contrib import admin

from core import models


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', ), }


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', ), }


admin.site.register(models.Blog)
admin.site.register(models.Author)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
