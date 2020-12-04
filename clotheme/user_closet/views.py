from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Closet

def indexx(request):
    all_closets = Closet.objects.all()
    return render(request, 'user_closet/index.html', {'all_closets': all_closets})

def detail(request, closet_id):
    closet = get_object_or_404(Closet, pk=closet_id)
    return render(request, 'user_closet/detail.html', {'closet': closet})