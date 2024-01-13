from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        psw = request.POST['password1']
        cpsw = request.POST['password2']
        if psw == cpsw:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email exists')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,password=psw,first_name=f_name,last_name=l_name,email=email)
                user.save()
                print("User created")
                return redirect('login')
        else:
            messages.info(request, "Password not match")
            return redirect('register')
        return redirect('/')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        psw = request.POST['password']
        user = auth.authenticate(username=username, password=psw)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid username or password")
            return redirect('login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
