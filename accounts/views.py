from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user( username=request.POST['username'], password=request.POST['password1'])
        auth.login(request, user)
        return redirect('home')
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenicate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html', {'error': "username or password is incorrect."})
    return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        redirect('home')
    return render(request,'login.html')
     