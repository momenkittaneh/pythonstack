from django.shortcuts import render, redirect

from .models import *
from django.contrib import messages


# Create your views here.


def index(request):

    context = {
        'users': User.objects.all()

    }

    return render(request, "index.html", context)


def success(request):
    context = {
        'users': User.objects.all(),
        'posts': message.objects.all(),
        
    }

    return render(request, "success.html", context)


def register(request):
    errors = User.objects.register_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    if request.POST['password'] != request.POST['cpassword']:
        return redirect('/')
    # pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    request.session['username'] = request.POST['email']
    User.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
    return redirect("/success")


def login(request):
    errors = User.objects.login_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')

    user = User.objects.filter(email=request.POST['email'])
    user2 = User.objects.filter(password=request.POST['password'])
    if user:
        if user2:
            if user2[0].password == request.POST['password']:
                request.session['username'] = user[0].email
                return redirect("/success")
            else:
                return redirect('/')

        return redirect('/')
    else:
        return redirect('/')


def logout(request):
    del request.session['username']
    return redirect('/')



def create_post(request):
    post = request.POST['post']
    message.objects.create(user_message=post)
    return redirect('/main_page')

