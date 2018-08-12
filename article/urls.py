from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'Article/$', views.articles, name='article'),
    url(r'article-column/$', views.article_column, name='article_column'),
    url(r'column-rename/$', views.rename_article_column, name='column_rename'),
    url(r'del-column/$', views.del_article_column, name='del_column'),
    url(r'article-post/$', views.article_post, name='article_post'),
    url(r'article-list/$', views.article_list, name='article_list'),
    url(r'article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.article_detail, name='article_details'),
    url(r'del-article/$', views.del_article, name='del_article'),
    url(r'edit-article/(?P<article_id>\d+)/$', views.edit_article, name='edit_article'),
    url(r'article-tag/$', views.article_tag, name='article_tag'),
    url(r'edit_tag/$', views.edit_tag, name='edit_tag'),
    url(r'del_tag/$', views.del_tag, name='del_tag'),
    url(r'detail/(?P<id>\d+)/(?P<slug>[-\w]+)$', views.detail, name='detail')
]
app_name = 'article'
