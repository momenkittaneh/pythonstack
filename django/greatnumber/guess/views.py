from django.shortcuts import redirect, render, HttpResponse
import random

num= random.randint(1, 100)

def index(request):
    global num
    if 'num' not in request.session:
        request.session['num']


    return render(request,'index.html')



def guessing(request):
    thenumber= int(num)
    gues = int(request.POST['thenum'])
    if gues == thenumber:
        context={
            'answer':1
        }
        
    if gues > thenumber:
        context={
            'answer':2
        }
        
    if gues < thenumber:
        context={
            'answer':3
        }
    return render(request,'index.html',context)



def clear(request):
    request.session.clear()
    request.session['num']=random.randint(1, 100)

    return redirect('/')
