from django.shortcuts import render
from django.http import HttpResponse



def index(request):
	return render(request, "givesmartapp/index.html", None)
    # return HttpResponse("Hello, world. You're at the polls index.")

def search(request):
	return render(request, "givesmartapp/search.html", None)
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
	return render(request, "givesmartapp/donate.html", None)
	# return HttpResponse("Donate page!")

def submit_donation(request):
	return render(request, "givesmartapp/submit_donation.html", None)
	# return HttpResponse("Submitting donation!")


