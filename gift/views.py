from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import item
#from xiuyun import forms
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def homepage(request):
    return render(request,"index.html",locals())