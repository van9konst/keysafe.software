from django.conf.urls import url

from keys import views

urlpatterns = [
    url(r'^$', views.MyView.as_view(), name='main'),
]