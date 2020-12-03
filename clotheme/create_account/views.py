from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def indd(request):
    return render(request, 'create_account.html')

