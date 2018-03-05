from django.shortcuts import render, redirect
from .models import Question, Document, Player
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

	u = User.objects.get(username=request.user)

	player = Player.objects.get(user=u)

	# print(u.player)

	try:
		_question = Question.objects.get(level=player.current_level)
	except:
		return HttpResponse("You have completed all Problems, Check out the Leaderboard!")

	# url = _question.outputfile.url
	# filenameurl = url[url.rfind("/")+1:] #extract filename from url

	#each directory/file should be single entity not like /media/output_files/


	print(_question.inputfile.url)

	keyword = str(_question.level) + '_output.txt'

	output_file = os.path.join(BASE_DIR, 'media', 'output_files', keyword)


	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():

			newdoc = Document(docfile = request.FILES['docfile'])
			request.FILES['docfile'].name = 'aman.txt'
			
			newdoc.save()


			fc = filecmp.cmp(settings.USER_OUTPUT_FILE, output_file)
			print(fc)
			

			os.remove(settings.USER_OUTPUT_FILE)	

			if(fc):
				player.current_level += 1
				player.score += 10
				player.timestamp=datetime.datetime.now()
				player.save()

				return redirect(question)

			else:
				messages.error(request, "Wrong Output!, Try Again")
				# return redirect(question)

			# print(request.FILES['docfile'].read())
			# print('\n\n')
			# print('from db')
			# print('\n\n')

			# print(question.answer)

			# print(question.answer == request.FILES['docfile'].read())



			# with open ("/home/aman/tknotes.txt", "r") as myfile:
			# 	data=myfile.readlines()
			# print(data)

			# Redirect to the document list after POST
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

	for key in request.session.keys():
		print(request.session[key])
		del request.session[key]
		print('deleted: ')

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