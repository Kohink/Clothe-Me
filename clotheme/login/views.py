from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def index(request):
    return HttpResponse("<h1> Login Page")


