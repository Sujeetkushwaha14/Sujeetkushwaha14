from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'index.html')



def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        my_user=User.objects.create_user(username,password)
        my_user.save()
    return render(request, 'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,Username=username,Password=password)
        
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return HttpResponse("user is not valide!!!")      
    
    return render(request, 'login.html')
@login_required()
def homepage(request):
    return render(request, 'homepage.html')

def loguot(request):
    logout(request)
    return render(request, 'login.html')