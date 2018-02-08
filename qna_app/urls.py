from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^question/(?P<q_title>\w+)/', views.question, name='question'),
    url(r'^logout/', 'qna_app.views.logout_view', name='logoutview'), 
] 