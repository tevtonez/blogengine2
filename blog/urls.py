from django.conf.urls import url
from blog import views


app_name = 'blog'
urlpatterns = [
  url(r'^$', views.PostListView.as_view(), name = 'post_list'),
  url(r'^about/$', views.AboutView.as_view(), name = 'about'),
  url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name = 'post_detail'),
  url(r'^post/new/$', views.CreatePostView.as_view(), name = 'post_new'),
  url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name = 'post_edit'),
  url(r'^post/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name = 'post_delete'),
  url(r'^drafts/$', views.DraftsListView.as_view(), name = 'post_draft_list'),
  url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name = 'add_comment_to_post'),
]
