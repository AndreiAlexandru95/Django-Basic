# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Choice, Question

# Register your models here.

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date', 'question_text']
	fieldsets = [
		(None, 					{'fields':['question_text']}),
		('Date Information',	{'fields':['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInLine]

	list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)

#admin.site.register(Choice)
