from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string1(request):
    return HttpResponse('<marquee bgcolor="lime"><h1>This is String Response</h1></marquee>')
