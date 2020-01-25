from django.shortcuts import render, redirect

from datetime import datetime
import random
from core.forms import ContUsForm
from core.models import feeed, Bots, Autor


def func_home(reqest):
	#students=['1','2','3']
	#v=random.randint(0,len(students)-1)
	#vall=students[v]
	return render(reqest,'home.html', context={'name':'Homan','now':datetime.now()
		#"students":['1','2','3'], 'random_val':vall
		})

def func_us(reqest):
	return render(reqest,'us.html')

def func_contus(reqest):
	LAST_MESSAGE='no message'

	form=ContUsForm(reqest.POST)

	if reqest.method=="POST":
		LAST_MESSAGE=reqest.POST.get('message')
		
		feedback=feeed.objects.create(name=reqest.POST.get("name"), text=LAST_MESSAGE)
		r=redirect('/feedbacks')
		r['Location']+='?from=contus'
		return r


	return render(reqest,'contus.html', context={'message':LAST_MESSAGE, "form":form})	

def func_feedbacks(reqest):
	feedbacks=feeed.objects.filter(is_active=True)

	has=bool(reqest.GET.get('from'))
#	feedbacks=feeed.objects.all()

	return render(reqest,'feedbacks.html', context={"feedbacks":feedbacks, 'has':has})

def func_bots(reqest):
	#bots=Bots.objects.filter(is_active=True)
	autor_name=reqest.GET.get('autor')
	if autor_name:
		autor=Autor.objects.filter(name=autor_name).first()
		bots=Bots.objects.filter(autor=autor,is_active=True)
	else:
		bots=Bots.objects.filter(is_active=True)

	return render(reqest,'bots.html', context={"bots":bots})



# Create your views here.
