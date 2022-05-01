from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def cs(request):
    return render(request,'cs.html')

def IS(request):
    name=request.GET['n1']
    return render(request,'is.html',{'n':name})

def ec(request):
    return render(request,'ec.html')

def reg(request):
    return render(request,'reg.html')