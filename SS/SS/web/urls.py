from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'web'

urlpatterns = [
    url(r'^$', views.detail, name='detail'),
    url(r'^about/$', views.aboutview, name='aboutview'),
    url(r'^publications/$', views.pubview, name='pubview'),
    url(r'^students/$', views.studentview, name='studentview'),
    url(r'^recognitions/$', views.recognitionview, name='recognitionview'),
    url(r'^projects/$', views.projectview, name='projectview'),
    url(r'^teachings/$', views.teachingsview, name='teachingview'),
    # url(r'^register/$', views.userformview.as_view(), name='register'),
    # url(r'^(?P<pk>[0-9]+)/$',views.detailview.as_view(), name='detail'),
    # url(r'album/add$',views.albumcreate.as_view(), name='album-add'),
    # url(r'album/add/(?P<pk>[0-9]+)/$',views.albumupdate.as_view(), name='album-update'),
    # url(r'album/add/(?P<pk>[0-9]+)/delete/$', views.albumdelete.as_view(), name='album-delete'),


]

