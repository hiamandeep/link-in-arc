from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=150,null=True)
	question = models.CharField(max_length=200)
	# answer = models.TextField(max_length=200)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')