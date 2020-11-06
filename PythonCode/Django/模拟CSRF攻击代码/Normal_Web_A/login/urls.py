from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    url(r'^transfer/$', views.Transfer.as_view()),
]