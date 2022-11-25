from django.shortcuts import render
from django.http import HttpResponse
from .models import Counter

def index(request):
    return HttpResponse(Counter.counter)

