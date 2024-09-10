from django.shortcuts import render,HttpResponse,redirect
from.models import Blog,comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# Create your views he

def home(request):


    bolg = Blog.objects.all()

    context = {
        "blog" :bolg
    }
    return render(request,"home.html",context)

def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")


def content(request,id):
    blog  = Blog.objects.get(id=id)
    
    context ={
        "blog":blog,
        
    }
    return render(request,"blogcontent.html",context)



def signup(request):
    if request.method=="POST":
        fname = request.POST.get("fname")
        email = request.POST.get("email")
        password = request.POST.get("password")


        User =User.objects.create_user(first_name=fname,username=email,email=email,password=password)

        User.save()
    

    return render(request,("signup.html"))




def Login(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = authenticate(request, username=email, password=password)
    if user is not None:
        messages.info(request, "successfully logind in...")
        login(request,user)
    else:
        pass  
    
    return render(request,"login.html")


def Logout(request):
    logout(request)
    return redirect("Home")

      
def comment(request):
    if request.method=="POST":
        name = request.user
        blog_id = request.POST.get("blogid")
        comment = request.POST.get("comment")
        blog=Blog.objects.get(id=blog_id)

        comment = comment(name=name,blogparent=blog,comment=comment)

        comment.save()
        messages.success(request,"comment Successlly added")
        return redirect(f"content/{blog_id}")

    
     