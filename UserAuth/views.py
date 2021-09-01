from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.utils.html import escape
from  .forms import OurSingUpForm,Userloginform,UserProfileUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout


# Create your views here.

# SignUp Page Logic
def singup(request):

    if request.method == "POST":
        userform = OurSingUpForm(request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect("login")
          
         
    else:
          userform = OurSingUpForm()
    
    return render(request,'UserAuth/signup.html' , {'userform':userform})







# Login page
def login_form(request):

    if request.method == "POST":

        authform = Userloginform(request=request, data = request.POST)

        if authform.is_valid():
            uname = authform.cleaned_data['username']
            upass = authform.cleaned_data['password']
            obj = authenticate(username = uname, password = upass)
            if obj is not None:
                login(request,obj)
          
                return HttpResponseRedirect("profile")
    
    else:

        authform = Userloginform()

    return render(request,'UserAuth/login.html',{'authform': authform})




# Logout


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("login")


#Profile Edit
def user_profile(request):

    if request.method == "POST":  
        profilefm = UserProfileUserForm(request.POST,instance = request.user)

        if profilefm.is_valid():
            profilefm.save()
            messages.success(request,"Profile Has been updated")
    else:

        profilefm = UserProfileUserForm(instance=request.user)

    return render(request, "UserAuth/profile.html",{'profilefm': profilefm})


