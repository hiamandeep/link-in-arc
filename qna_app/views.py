from django.shortcuts import render, redirect
from .models import Question, Document, Player, TotalProblem
from .forms import DocumentForm
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
import filecmp
import os
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.

def home(request):
	return render(request,'home.html',{'active_h':'active'})

@login_required
def question(request):

	totalprob = TotalProblem.objects.get(id=1)
	lastprob = totalprob.totalproblem

	u = User.objects.get(username=request.user)

	player = Player.objects.get(user=u)



	try:
		_question = Question.objects.get(level=player.current_level)
	except Question.DoesNotExist:
		if player.current_level > lastprob:
			return render(request, 'complete.html', {'active_q':'active'})
		return render(request, 'finish.html', {'active_q':'active'})


	out_url = _question.outputfile.url

	out_url = out_url.split('/')
	print(out_url)
	out_url = os.path.join(os.path.dirname(BASE_DIR), out_url[0], out_url[1], out_url[2], out_url[3])



	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():

			newdoc = Document(docfile = request.FILES['docfile'])
			
			newdoc.save()


			user_out_url = newdoc.docfile.url.split('/')

			user_out_url = os.path.join(os.path.dirname(BASE_DIR), user_out_url[0], user_out_url[1], user_out_url[2], user_out_url[3])


			# fc = filecmp.cmp(user_out_url, out_url)

			f1 = open(user_out_url, "r").read()
			f2 = open(out_url, "r").read()
			fc = f1 == f2


			print(fc)
			

			# os.remove(settings.USER_OUTPUT_FILE)	

			if(fc):
				player.current_level += 1
				player.score += 10
				player.timestamp=datetime.datetime.now()
				player.save()
				_question.numuser = _question.numuser + 1
				_question.accuracy = round(_question.numuser/(float(_question.numuser + _question.wrong)),2)
				_question.save()

				return redirect(question)

			else:
				_question.wrong = _question.wrong + 1
				_question.save()				
				messages.error(request, "Wrong Output!, Try Again")


	else:
		form = DocumentForm() 
	
	return render(request, 'question.html', {'question':_question,'form': form, 'player': player, 'active_q': 'active'})


def leaderboard(request):

	players = Player.objects.order_by('-score','timestamp')
	
	rank_counter = 1

	for player in players:
		player.rank = rank_counter
		rank_counter += 1

	return render(request, 'leaderboard.html', {'players': players, 'active_l':'active'})



def logout_view(request):

	logout(request)
	return redirect("home")


def save_profile(backend, user, response, *args, **kwargs):
	if backend.name == 'facebook':
		try:
			player = Player.objects.get(user=user)
		except:
			player = Player(user=user)
			player.name = response.get('name')
			player.timestamp=datetime.datetime.now()
			player.save()
	elif backend.name == 'google-oauth2':
		try:
			player = Player.objects.get(user=user)
		except:
			player = Player(user=user)
			player.timestamp=datetime.datetime.now()
			player.name = response.get('name')['givenName'] + " " + response.get('name')['familyName']
			player.save()

