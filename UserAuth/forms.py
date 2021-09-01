from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import widgets
from django import forms






class OurSingUpForm(UserCreationForm):

    password1 = forms.CharField(label='password',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='password Again',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
        labels = {'email': "Email"}


        widgets = {

            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),

            
        }

   

class Userloginform(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'nickname', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password','class': 'form-control'}))
    
    class Meta:
        model = AuthenticationForm
        fields = ('__all__')



class UserProfileUserForm(UserChangeForm):

    password = None
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','last_login','date_joined',)
        labels = {'email': "Email"}



        widgets = {

            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'last_login' : forms.DateInput(attrs={'class':'form-control'}),
            'date_joined' : forms.DateInput(attrs={'class':'form-control'}),

            
        }
