from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import MainappOrder

def backgroun_job():
	# scheduler = BackgroundScheduler()
	# sched = BackgroundScheduler()
	# sched.add_job(scrapper())

	# sched.start()
    pass
def test(request):
    p = MainappOrder(channel="sk", brand="alkaram alarabi")
    p.save()
    return HttpResponse("return this string")
