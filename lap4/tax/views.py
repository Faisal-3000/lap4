from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tax_rate = 0.15

def index(request):
    return HttpResponse("this is a site to calculate tax!")

def tC(request,cost):
    cost = int(cost)
    finalcost = (cost * tax_rate) + cost
    return HttpResponse("The price after 15% tax : ",finalcost)

def tR(request):
    return HttpResponse(f"<h1> {tax_rate*100}% </h1>")