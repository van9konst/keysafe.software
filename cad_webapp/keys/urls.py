from django.conf.urls import url

from keys import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]