from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request , "index.html",{})


def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request , username = username , password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Worng details try again or sign up ")
            return redirect('login')
    else:    
        return render(request,"login.html",{})

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')  
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('signup') 
            else:
                user = User.objects.create_user(username = username,email = email ,password = password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password does not match')
            return redirect('signup')
    else:
        return render(request,"signup.html",{})
    
def logout(request):
    auth.logout(request)
    return redirect("/")

