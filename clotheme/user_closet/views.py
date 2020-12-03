from django.http import HttpResponse
from django.shortcuts import render
from .models import Closet

def indexx(request):
    all_closets = Closet.objects.all()
    context = {'all_closets': all_closets}
    return render(request, 'user_closet/index.html', context)

def detail(request, closet_id):
    return HttpResponse("<h2>This is the User Closet: " + str(closet_id) + "</h2>")