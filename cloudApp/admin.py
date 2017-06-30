# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date', 'question_text']
	fieldsets = [
		(None, 					{'fields':['question_text']}),
		('Date Information',	{'fields':['pub_date']}),
	]

admin.site.register(Question, QuestionAdmin)
