from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=150,null=True)
	question = models.CharField(max_length=200)
	inputfile = models.FileField(upload_to='input_files/', default='def_in')

	def __str__(self):
		return self.title


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')