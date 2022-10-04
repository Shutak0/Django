from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('latest/', views.latest,name='latest'),
    path('faq/', views.faq,name='faq'),
    path('popular/', views.popular,name='popular'),
    path('comments/', views.comments, name='comments'),
    path('kartinka', views.ckartinka, name='ckartinka'),
    path('send/', views.send, name='send')
]