from django.db import models
from datetime import datetime

# Create your models here.

class feeed(models.Model):
	name=models.CharField(max_length=32)
	text=models.CharField(max_length=50)
	created=models.DateTimeField(auto_now_add=True)
	is_active=models.BooleanField(default=False)

	class Meta:
		ordering=['-created']

	def __str__(self):
		return f'{self.name} - {self.text} {self.created}'

class Autor(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	webpage=models.CharField(max_length=100)
	

	def __str__(self):
		return f'Autor {self.name}'

class Bots(models.Model):
	name=models.CharField(max_length=32)
	bot_name=models.CharField(max_length=32)
	description=models.CharField(max_length=100)
	is_active=models.BooleanField(default=False)
	autor=models.ForeignKey(Autor, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f'Bot {self.name}'

