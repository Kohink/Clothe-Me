from django.http import HttpResponse
from .models import Closet

def indexx(request):
    all_closets = Closet.objects.all()
    html = ''
    for closet in all_closets:
        url = '/closet/' + str(closet.id) + '/'
        html += '<a href="' + url + '">' + closet.name + '</a><br>'
    return HttpResponse(html)

def detail(request, closet_id):
    return HttpResponse("<h2>This is the User Closet: " + str(closet_id) + "</h2>")