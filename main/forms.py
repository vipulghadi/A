from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
#this import is to get bulitin signup form
from django.contrib.auth.models import User
# this import is for accessing all field ,which user have
from django import forms
from .models import BlogPost



class Userform(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(label="re-enter password",widget=forms.PasswordInput())
    class Meta():
        model=User

        fields=["username","first_name","last_name","email"]
        
        
        
class AddBlog(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields="__all__"
        widgets={"Title":forms.TextInput(attrs={"class":"form-control"})}


   


        
     
        
        