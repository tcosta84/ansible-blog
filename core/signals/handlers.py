from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.cache import cache

from core import models, tasks


@receiver(post_delete, sender=models.Article)
@receiver(post_save, sender=models.Article)
def delete_article_cache(sender, **kwargs):
    tasks.delete_article_cache.delay()


@receiver(post_delete, sender=models.Blog)
@receiver(post_save, sender=models.Blog)
def delete_blog_cache(sender, **kwargs):
    tasks.delete_blog_cache.delay()
