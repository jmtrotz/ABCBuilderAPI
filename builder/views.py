import subprocess, os

#from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from builder.models import Builder
from builder.serializers import BuilderSerializer
from django.shortcuts import render
from django.conf.urls import url
from builder import views

# Create your views here.
@csrf_exempt

# Runs a script for syncing ABC source code with GitHub
def syncSource(request):
    if request.method == 'GET':
        subprocess.Popen("./syncSource.sh", cwd="/home/jeff/ABC/")
        status = "Sync started!"
        return JsonResponse(status, safe=False)

@csrf_exempt

# Runs a script to compile ABC source code
def buildROM(request):
    if request.method == 'GET':
        subprocess.Popen("./buildROM.sh", cwd="/home/jeff/ABC/")
        status = "Build started!"
        return JsonResponse(status, safe=False)
