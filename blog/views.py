from django.shortcuts import render,HttpResponseRedirect
from .forms import BlogForm
from .models import Blog_model
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home_page(request):
    hp = Blog_model.objects.all()
    return render(request,"blog/home.html", {'hp':hp})

def add_blog(request):
        if request.method == "POST":
            print(request.user.id)
            fm = BlogForm(request.POST)
            if fm.is_valid():
                tit = fm.cleaned_data['title']
                bod = fm.cleaned_data['body']
                aut = fm.cleaned_data['author']
                fm = Blog_model(title= tit, body = bod, author = aut,)
                fm.save()
                return HttpResponseRedirect("/")
        else:
            fm = BlogForm()
        return render(request,"blog/AddBlog.html", {'fm':fm})
  

def PostDetail(request,id):

    post = Blog_model.objects.get(pk=id)

    return render(request,"blog/detail.html", {'post':post})


def editblog(request,id):
    if  request.method == "POST":
        EditModel = Blog_model.objects.get(pk=id)
        editform = BlogForm(request.POST, instance=EditModel)
        if editform.is_valid():
            editform.save()
            return HttpResponseRedirect("/")
    else:
        EditModel = Blog_model.objects.get(pk=id)
        editform = BlogForm(instance=EditModel)

    
    return render(request, "blog/editblog.html", {'editform':editform} )



def deletblog(request,id):

    blog_delete = Blog_model.objects.get(pk=id)

    blog_delete.delete()
    return HttpResponseRedirect("/")



def dashboard(request):

    hp = Blog_model.objects.all()



    return render(request,"blog/dashboard.html",{'hp':hp})


    


