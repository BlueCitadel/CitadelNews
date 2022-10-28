import os
import google_apis_oauth

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect


def project(request):
    return render(request, 'login.html', {})

def dashboard(request):
    return render(request, 'index.html', {})
