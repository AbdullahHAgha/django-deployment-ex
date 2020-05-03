from django.conf.urls import url
from basicApp import views

#for template tagging
app_name = 'basicApp'

urlpatterns = [
    url(r'^other/$',views.other,name='other'),
    url(r'^relative/$',views.relative,name='relative'),
]
