from django.shortcuts import redirect, render
from .models import *

def index(request):
    return redirect("/shows")

def display(request):
    context={
        'sho' : show.objects.all()
    }
    return render(request,'shows.html',context)

def addshow(request):

    show.objects.create(title=request.POST['name'],network=request.POST['netw'],release_date= request.POST['relea'],desc=request.POST['desc'])
    return redirect('/')



def vadd(request):
    return render(request,'addshow.html')

def edit(request,id):
    x=id
    context={
        'sh' : show.objects.get(id=x)
    }
    return render(request,"editshow.html",context)

def upd(request,id):
    sh= show.objects.get(id=id)
    sh.title= request.POST['ti']
    sh.network=request.POST['net']
    sh.re=request.POST['date']
    sh.desc=request.POST['desc']
    sh.save()
    return redirect("/")
def showing(request,id):
    context={
        'sh':show.objects.get(id=id)
    }
    return render(request,'displayshow.html',context)