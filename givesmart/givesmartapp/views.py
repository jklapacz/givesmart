from django.shortcuts import render
from django.http import HttpResponse
from .classes import *
from . import data


def index(request):

	return render(request, "givesmartapp/index.html", None)
    # return HttpResponse("Hello, world. You're at the polls index.")

def search(request):
	print data.charities[0]
	context = {
		'charities':list()
	}
	for c in data.charities:
		context['charities'].append(c)

	return render(request, "givesmartapp/search.html", context)
	# return HttpResponse("Search page!")

def compare(request):
	return render(request, "givesmartapp/compare.html", None)
	# return HttpResponse("Compare page!")

def view_charity(request, name):
	resp = "Charity " + str(name)
	context = {
		'charity':resp
	}
	return render(request, "givesmartapp/charity.html", context)
	# return HttpResponse(resp)

def donate(request):
# def donate(request, donate_name):
	# print donate_name
	return render(request, "givesmartapp/donate.html", None)
	# return HttpResponse("Donate page!")

def submit_donation(request):
	return render(request, "givesmartapp/submit_donation.html", None)
	# return HttpResponse("Submitting donation!")


