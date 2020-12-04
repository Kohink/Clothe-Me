from django.http import Http404
from django.shortcuts import render
from .models import Closet

def indexx(request):
    all_closets = Closet.objects.all()
    return render(request, 'user_closet/index.html', {'all_closets': all_closets})

def detail(request, closet_id):
    try:
        closet = Closet.objects.get(pk=closet_id)
    except Closet.DoesNotExist:
        raise Http404("Closet does not exist")
    return render(request, 'user_closet/detail.html', {'closet': closet})