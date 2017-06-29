# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
#from django.template import loader
#from django.http import Http404

from .models import Choice, Question

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

#def detail(request, question_id):
#	try:
#		question = Question.objects.get(pk = question_id)
#	except Question.DoesNotExist:
#		raise Http404("Question does not exist")
#	return render(request, 'cloudApp/detail.html', {'question': question})

# Shortcut version of the above
def detail(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'cloudApp/detail.html', {'question': question})

def results(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'cloudApp/results.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting from
		return render(request, 'cloudApp/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing with POST data
		# Prevent data from being posted twice if a user hits the back button
		return HttpResponseRedirect(reverse('cloudApp:results', args=(question.id,)))