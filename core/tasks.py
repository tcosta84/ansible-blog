from django.core.cache import cache

from celery import shared_task


@shared_task(bind=True)
def delete_article_cache(self):
    print 'Celery: deleting article cache ...'
    cache.delete('article_list')

@shared_task(bind=True)
def delete_blog_cache(self):
    print 'Celery: deleting blog cache ...'
    cache.delete('blog')
