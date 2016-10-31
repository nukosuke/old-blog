from django.conf.urls import url
from . import views

urlpatterns = [
    # pages
    url(r'^new/edit$', views.new_edit, name='entry-new-edit'), # new entry editor page
    url(r'^(?P<slug>.+)/edit$', views.edit, name='entry-edit'), # exists entry editor page

    # post endpoint
    url(r'^new$', views.new, name='entry-new'),
    url(r'^(?P<entry_id>\d+)/update$', views.update, name='entry-update'), # update exists entry
    url(r'^(?P<entry_id>\d+)/delete$', views.delete, name='entry-delete'), # delete entry

    url(r'^(?P<slug>.+)$', views.show, name='entry-show'),
]
