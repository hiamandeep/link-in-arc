from django.contrib.auth.models import User

from django.db import models

# Create your models here.


class Question(models.Model):
	level = models.IntegerField(blank=False, null=True)
	title = models.CharField(max_length=150, null=True)
	question = models.TextField(null=True)
	inputfile = models.FileField(upload_to='input_files/', default='def_in')
	outputfile = models.FileField(upload_to='piQtH987P/', default='def_out')
	numuser = models.IntegerField(default=0)
	accuracy = models.FloatField(default=0)
	wrong = models.IntegerField(default=0)
	
	def __str__(self):
		return self.title


class Player(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	name = models.CharField(max_length=128,null=True)
	current_level = models.IntegerField(default=1)
	score = models.IntegerField(default=0)
	timestamp = models.DateTimeField(null=True)

	def __str__(self):
		return self.user.username


class Document(models.Model):
	docfile = models.FileField(upload_to='XuTz8iWw/')	

class TotalProblem(models.Model):
	totalproblem = models.IntegerField(default=100)

	def __str__(self):
		return str(self.totalproblem)
