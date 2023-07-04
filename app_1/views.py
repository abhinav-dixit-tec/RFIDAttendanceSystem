from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def start(request):
    return redirect('login')
    # return HttpResponse("<a href='/login'>Login</a>")
def logout(request):
    auth.logout(request)
    return redirect('login')

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        # return HttpResponse("<a href='/logout'>Logout</a><a href='/change_pass'>change password</a>")

    if request.method == 'POST':        
        email = request.POST['email_field']
        password = request.POST['pass_field']
        user  = auth.authenticate(username=email, password = password)
        if user is not None:
            ob = User.objects.get(username = user)
            print(ob.is_superuser)            
            auth.login(request, user)
            return redirect('dashboard')
            # return HttpResponse("<a href='/logout'>Logout</a><a href='/change_pass'>change password</a>")# go to dashboard
        
    
    return render(request, 'app_1/new_login.html')

def change_pass(request):
    if request.method == 'POST' and request.user.is_authenticated:                
        #check old password        
        if auth.authenticate(username = request.user.username, password = request.POST['old_pass_field']):
            if request.POST['new_pass_field_1'] == request.POST['new_pass_field_2']:
                u = request.user
                print(request.POST['new_pass_field_1'])
                u.set_password(request.POST['new_pass_field_1'])
                u.save()

                messages.success(request, 'Password Changed successfully !')
            else:
               messages.error(request, 'Confirm Password does not match')
        else:
            messages.error(request, 'Invalid Old password') 
        return render(request, 'app_1/change_pass.html')
        #check pass1 and pass2        
    if(request.user.is_authenticated):
        return render(request, 'app_1/change_pass.html')