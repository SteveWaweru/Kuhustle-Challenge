from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def users(request):
    user = User.objects.all()
    return HttpResponse(user)

def jobs(request):
    job = Job.objects.all()
    return HttpResponse(job)

def bids(request):
    bid = Bid.objects.all()
    return HttpResponse(bid)

def name(request, n):
    user = User.objects.filter(username = n)
    return HttpResponse(user)