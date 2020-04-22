from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    # url(r'^$',            views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),         # Вариант на Class-based views
    path('',              views.post_list, name='post_list'),         # Вариант на "общих" представлениях (views)

    # url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),  # теги исходное
    path('tag/<slug:tag_slug>/',        views.post_list, name='post_list_by_tag'),  # теги 1

    # url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',views.post_detail, name='post_detail'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>/',                 views.post_detail, name='post_detail'),

    # url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    path('blog/<int:post_id>/share/', views.post_share, name='post_share'),
]
