# -*- coding: utf-8 -*-

from django.http import HttpResponse

def home(request):

	return HttpResponse('olá')

def contact(request):

	return HttpResponse('contact')