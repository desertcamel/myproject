from django.conf.urls import include, url

from boards import views

urlpatterns = [
    url(r'^$', views.BoardListView.as_view(), name='boards-index'),
    url(r'^boards/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),    
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    url(r'^boards/new_post/$', views.NewPostView.as_view(), name='new_post'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
    views.PostUpdateView.as_view(), name='edit_post'),
]



