from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from django.http import request
# Create your views her
from . import index1

def index(request):
    if request.method == 'POST':
        k1=index1.get_audio(request.POST.get('transcript'))
        con={
            'a':k1,
        }
        return render(request,'index.html',con)
    else:
        con={
            'a':"Hello",
        }
        return render(request,'index.html',con)
