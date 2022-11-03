from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Blog, Profile


def home(request):
    data = Blog.objects.all()
    return render(request, "home.html", {"data": data})


def posts(request, id):
    data = Blog.objects.get(id=id)
    return render(request, 'posts.html', {"data": data})


def profile(request, id):
    data = Profile.objects.get(user_id=id)
    return render(request, 'profile.html', {"data": data})


def profile_form(request):
    return render(request, 'createprofile.html')


def createprofile(request):
    p = Profile()
    p.name = request.POST.get("name")
    p.surname = request.POST.get("surname")
    p.occupation = request.POST.get("occupation")
    p.address = request.POST.get("address")
    p.mobile = request.POST.get("mobile")
    pk = request.user.id
    user = User.objects.get(id=pk)
    p.user = user

    p.save()
    messages.success(request, "Create Profile")
    return redirect("/home")


def createblog(request):
    return render(request, "createblog.html")


def editprofile(request, id):
    data = Profile.objects.get(user_id=id)
    return render(request, 'editprofile.html', {"data": data})


def updateprofile(request, id):
    p = Profile.objects.get(id=id)
    p.name = request.POST.get("name")
    p.surname = request.POST.get("surname")
    p.occupation = request.POST.get("occupation")
    p.address = request.POST.get("address")
    p.mobile = request.POST.get("mobile")

    p.save()
    messages.success(request, "updated Profile")
    return redirect("/home")


def myblog(request, id):
    b = Blog.objects.filter(pro_user_id=id)
    return render(request, "myblog.html", {"data": b})

def editblog(request,id):
    #data=Blog.objects.get(pro_user_id=id)
    data = Blog.objects.get(id=id)
    return render(request,"editblog.html", {"data":data})

def updateblog(request, id):
    b= Blog.objects.get(id=id)
    b.name = request.POST.get("name")
    b.description = request.POST.get("description")
    b.author = request.POST.get("author")
    b.imgpath = request.POST.get("imgpath")


    b.save()
    messages.success(request, "update blog")
    return redirect("/home")