from django.conf.urls import patterns, url

from core import views


urlpatterns = patterns('',
    url(r'^$', views.ArticleListView.as_view(), name='article-list'),
    url(r'^posts/(?P<slug>[-_\w]+)/$', views.ArticleDetailView.as_view(), name='article-detail'),
    url(r'^categories/(?P<slug>[-_\w]+)/$', views.CategoryDetailView.as_view(), name='category-detail'),
)
