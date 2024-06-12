from django.shortcuts import render
from django.http import  HttpResponse ,HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from usertable.models import User
import time

def register_view(request):
    if request.method == "GET":
        return render(request, 'usertable/register.html')
    elif request.method == 'POST':
        reg_username = request.POST['username']
        password0 = request.POST['password0']
        password1 = request.POST['password1']
        if password0 == password1 and len(password0) != 0 and len(reg_username) != 0:
            u1 = User.objects.filter(username=reg_username).first()
            if u1 is None:
                date = time.strftime('%Y-%m-%d %H:%M:%S')
                r1 = User(username=reg_username, password=make_password(password1), reg_date=date)
                r1.save()
                return HttpResponseRedirect('login')
            else:
                return render(request, 'usertable/register.html')
        else:
            return render(request, 'usertable/register.html')


def login_view(request):
    if request.method == "GET":
        return render(request, 'usertable/login.html')
    elif request.method == "POST":
        login_user = request.POST['username']
        login_pass = request.POST['password0']
        result_user = User.objects.filter(username=login_user).first()
        print(result_user.password)
        global user
        user = login_user
        if login_user == 'admin' and check_password(login_pass, result_user.password):
            return HttpResponseRedirect('/admin_server/index')
        elif result_user is not None and check_password(login_pass, result_user.password):
            return HttpResponseRedirect('home')
        else:
            return render(request, 'usertable/login.html')

def home_view(request):
    show_user = user
    date = User.objects.get(username=show_user).reg_date
    return render(request, 'usertable/home.html', locals())