from django.shortcuts import render
from django.http import HttpResponse
from .classes import *
from . import data
import os
import re

from django.template.defaulttags import register

@register.filter
def get_id(charity):
	return charity.initials

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def checkIfSearch(request):
	if 'search' in request.GET:
		return searchByTerm(request)
	elif 'category' in request.GET:
		return searchByCategory(request)
	else:
		return False

def account(request):
	context = {
		'charities':list(),
		'amounts':list(),
	}
	for c in data.account1.liked:
		context['charities'].append(c[0])
		context['amounts'].append(c[1])
	return render(request, "givesmartapp/account.html", context)

def searchByTerm(request):
	context = {
		'charities':list()
	}
	searchterm = request.GET['search']
	searchterm = searchterm.lower()
	expr = re.compile(searchterm)
	matches = list()
	for c in data.charities:
		curr_name = c.name.lower()
		if expr.search(curr_name) != None:
			context['charities'].append(c)
	return render(request, "givesmartapp/search.html", context)

def searchByCategory(request):
	context = {
		'charities':list()
	}
	category = request.GET['category']
	matches = data.categories[category]
	for c in matches:
		context['charities'].append(c)
	return render(request, "givesmartapp/search.html", context)

def index(request):
	context = {
		'charities':list()
	}
	result = checkIfSearch(request)
	if result != False:
		return result	
	else:
		for c in data.recommended:
			context['charities'].append(c)	
		return render(request, "givesmartapp/index.html", context)
	
    # return HttpResponse("Hello, world. You're at the polls index.")

def search(request):
	
	result = checkIfSearch(request)
	if result != False:
		return result
	else:

		context = {
			'charities':list()
		}
		for c in data.charities:
			
			context['charities'].append(c)

		return render(request, "givesmartapp/search.html", context)
	# return HttpResponse("Search page!")

def compare(request):
	# print request
	result = checkIfSearch(request)
	if result != False:
		return result
	context = {
		'charities':list()
	}
	query = request.POST
	mydict = dict(request.POST)
	list_to_compare = mydict['charity']
	for value in mydict['charity']:
		for c in data.charities:
			if value == c.initials:
				context['charities'].append(c)
	
	return render(request, "givesmartapp/compare.html", context)
	# return HttpResponse("Compare page!")

def view_charity(request, name):
	result = checkIfSearch(request)
	if result != False:
		return result

	context = {
		'charity':None
	}
	for c in data.charities:
		if c.initials == name:
			context['charity'] = c
	return render(request, "givesmartapp/charity.html", context)
	# return HttpResponse(resp)

def donate(request):
# def donate(request, donate_name):
	# print donate_name
	result = checkIfSearch(request)
	if result != False:
		return result
	# print request
	# for key in request:
	# 	print key
	context = {
		'charity':None,
		'amount': request.POST['amount']
	}
	for c in data.charities:
		if c.initials == request.POST['charity']:
			context['charity'] = c
	print context
	return render(request, "givesmartapp/donate.html", context)
	# return HttpResponse("Donate page!")

def submit_donation(request):
	result = checkIfSearch(request)
	if result != False:
		return result
	context = {
		'charity': None,
		'amount': request.POST['amount']
	}
	if context['amount'] == '':
		context['amount'] = 0
	for c in data.charities:
		if c.initials == request.POST['charity']:
			context['charity'] = c
	if request.POST['submission'] == 'Cancel':
		return render(request, "givesmartapp/charity.html", context)	
	return render(request, "givesmartapp/submit_donation.html", context)
	# return HttpResponse("Submitting donation!")


