# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    return render(request, 'personal/home.html') # for future reference, if you start w/personal_page, maintain that consistancy
# Create your views here.

def contact(request):
    return render(request, 'personal/contact.html')
