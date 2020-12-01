from django.http import HttpResponse

def indexx(request):
    return HttpResponse("<h1>This is the User Closet</h1>")
