from django import forms
from django.forms import widgets
from django.forms.models import ModelForm
from .models import Blog_model


class  BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog_model
        fields = ("title","body","author")

        widgets = {
            'title' :  forms.TextInput(attrs={'class':'form-control'}),
            'body' :  forms.Textarea(attrs={'class':'form-control'}),
        }


