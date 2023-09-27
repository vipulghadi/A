from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import Userform,AddBlog
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,update_session_auth_hash,authenticate
from .models import BlogPost
from django.contrib.auth.models import User
from datetime import date
from django.http.request import QueryDict, MultiValueDict
# Create your views here.
#home 
def home(request):
    return render (request,'main/home.html')


def blogs(request):
    
    blogs=BlogPost.objects.all()
    return render (request,'main/blogs.html',{"blogs":blogs})



#Sign Up page

def user_signup(re):
    if not re.user.is_authenticated:
        error=None
        if re.method =="POST":
            print(re.method)
            form=Userform(re.POST)
            if form.is_valid():
                form.save()
            
                error="Account Created Succesfully"
                form=Userform()
            else:
                error="please Enter Valid Details"
                form=Userform()
        else:
            print(re.method)
            form=Userform()
                    
        return render (re,'main/signup.html',{"form":form,"error":error})
    else:
        return HttpResponseRedirect('/dashboard/')

#log in 
def user_login(request):
    if  not request.user.is_authenticated:
        error=None
        if request.method=="POST":
            form=AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data["username"]
                upass=form.cleaned_data["password"]
                user=authenticate(username=uname,password=upass)
                if user is not None:#if user is valid we have to log in
                    login(request,user)
                    return HttpResponseRedirect("/blogs/")
                else:
                    error="please enter valid username and password"
                    form=AuthenticationForm()    
            else:
                error="please enter valid username and password"
                form=AuthenticationForm() 
        else:
            form=AuthenticationForm()
            
        return render(request,'main/login.html',{"form":form,"error":error})
    else:
        return HttpResponseRedirect('/blogs/')
    
    
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')
    
    
def user_dashborad(request):
    if request.user.is_authenticated:
        a=request.user.username
        user_info=User.objects.filter(username=a)
        user_blogs=BlogPost.objects.filter(author=a)
       
        return render(request,'main/dashboard.html',{"a":a,'userblogs':user_blogs,"user_info":user_info})
    else:
        return HttpResponseRedirect('/login/')
    
    
    
def add_blog(request):
    error=None
    if request.user.is_authenticated:
        if request.method=="POST":
            d=request.POST.dict()
            d["author"]=str(request.user);
            form=AddBlog(d)
            
            if form.is_valid():
                form.save()
                form=AddBlog()
                error="Blog Created Successfully"
            else:
                print("Not saved")
                error="Please Enter valid Data" 
        else:
            form=AddBlog()
            
        return render (request,'main/addblog.html',{"form":form,"error":error})
    
    else:
        return HttpResponseRedirect('/login/') 
   
    
def update_blog(request,id):
    error=None
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=BlogPost.objects.get(pk=id)
            d=request.POST.dict()
            d["author"]=str(request.user);
            form=AddBlog(d,instance=pi)
            if form.is_valid():
                form.save()
                error="Blog Updated Successfully"
            else:
                error="invalid blog"
                pi=BlogPost.objects.get(pk=id)
                form=AddBlog(instance=pi)
                   
        else:
            pi=BlogPost.objects.get(pk=id)
            form=AddBlog(instance=pi)
        
        return render(request,'main/updateblog.html',{"form":form,"error":error})    
            
       
    else:
        return HttpResponseRedirect('/login/')
    

def delete_blog(request,id):
    if request.user.is_authenticated:
        pi=BlogPost.objects.get(pk=id)
        pi.delete();
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
        
        
        
    