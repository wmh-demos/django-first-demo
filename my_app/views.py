from django.http import HttpResponse

def func(request):
    return HttpResponse("This is my first django project!")

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))