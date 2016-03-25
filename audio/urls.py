from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tuneforme/', views.TuneForMe, name='TuneForMe'),
    url(r'^newscard/', views.NewsCard, name='NewsCard'),
]