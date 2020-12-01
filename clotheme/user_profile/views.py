from django.http import HttpResponse

def ind(request):
    return HttpResponse("<h1>This is the User Profile</h1>")