from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^say/', views.say),
    url(r'^sayhello/', views.sayhello),
    url(r'^reverse/', views.to_rv, name='reverse'),
    url(r'^t_params/', views.t_params),
    # url(r'^t_json/', views.t_json1),
]