
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test1fun(request):
    return HttpResponse('heloo  cyber square')

def cyberfun(request):
    return render(request,'cyber.html')