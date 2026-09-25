from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>بسم الله الرحمن الرحيم</h1>")