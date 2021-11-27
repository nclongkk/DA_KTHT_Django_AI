from django.conf.urls import url
from FacerecogApp import views

urlpatterns=[
    url(r'^train$', views.train),
    url(r'^identify$', views.identify)
]