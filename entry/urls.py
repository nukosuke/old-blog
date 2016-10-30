from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='entry-index'),
    url(r'^(?P<entry_id>\d+)/edit$', views.edit, name='entry-edit'),
    url(r'^(?P<slug>.+)$', views.show, name='entry-show'),
]
