# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse

def index(response):
    return render(request, 'personal_page/home.html')
# Create your views here.
