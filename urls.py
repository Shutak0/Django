from django.urls import include, re_path
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('latest/', views.latest,name='latest'),
    path('faq/', views.faq,name='faq'),
    path('popular/', views.popular,name='popular'),
    path('postik/', views.postik, name='postik'),
    path('kartinka', views.ckartinka, name='ckartinka'),
    path('send/', views.send, name='send'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.post, name='post')
]