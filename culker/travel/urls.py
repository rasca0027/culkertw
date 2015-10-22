from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'list/', views.list, name='list'),
    url(r'story/(?P<story_id>[0-9]+)/$', views.story, name='story'),
    url(r'help/$', views.help, name='help'),
    url(r'about/$', views.about, name='about'),
]
