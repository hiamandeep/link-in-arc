from django.conf.urls import url

from qna_app.views import home ,logout_view, question, leaderboard

urlpatterns = [
	url(r'^$', home, name='home'),	
    url(r'^question/', question, name='question'),
    url(r'^leaderboard/$', leaderboard , name='leaderboard'),
    url(r'^logout/', logout_view, name='logoutview'), 
]