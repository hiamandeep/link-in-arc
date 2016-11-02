from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^question/(?P<q_num>\d+)/', views.question, name='question'),
] 