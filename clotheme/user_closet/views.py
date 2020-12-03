from django.http import HttpResponse
from .models import Closet

def indexx(request):
    return HttpResponse("<h1>This is the User Closet</h1>")

def detail(request, closet_id):
    return HttpResponse("<h2>This is the User Closet: " + str(closet_id) + "</h2>")