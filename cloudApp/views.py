# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
from django.http import Http404

from .models import Question

# Create your views here.

#def index(request):
#	#Display the latest 5 poll questions in the system 
#	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#	template = loader.get_template('cloudApp/index.html')
#	context = {
#		'latest_question_list': latest_question_list,
#	}
#	return HttpResponse(template.render(context, request))

# Short version of the above - without using django.template
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'cloudApp/index.html', context)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk = question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'cloudApp/detail.html', {'question': question})

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)