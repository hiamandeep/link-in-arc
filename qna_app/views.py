from django.shortcuts import render
from .models import Question, Document
from .forms import DocumentForm
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
import filecmp
import os
from django.conf import settings
# Create your views here.


def home(request):
	return render(request,'home.html',{})

def question(request, q_num):

	try:
		question = Question.objects.get(id=q_num)
	except:
		raise Http404


	if request.method == 'POST':
	    form = DocumentForm(request.POST, request.FILES)
	    if form.is_valid():

	        newdoc = Document(docfile = request.FILES['docfile'])
	        request.FILES['docfile'].name = 'aman.txt'
	        
	        newdoc.save()


	        fc = filecmp.cmp(settings.INPUT_FILE,settings.OUTPUT_FILE)
	        print(fc)
	        

	        os.remove(settings.INPUT_FILE)

	        if(fc):
	        	return HttpResponse("Correct!!")
	        else:
	        	return HttpResponseRedirect('#')

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
	
	return render(request, 'question.html', {'q_num':q_num, 'question':question,'form': form})