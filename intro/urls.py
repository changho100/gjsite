from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<item_id>\d{1,})/(?P<tab_id>\d{1,})$', views.item),
    url(r'^map$', views.map),
    url(r'^boarding$', views.boarding),
    url(r'^items$', views.items),
    url(r'^(?P<item_id>\d{1,})/video/(?P<video_id>\d{1,})$', views.video),
]