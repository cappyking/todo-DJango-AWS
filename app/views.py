from multiprocessing import context

from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginUser,logout
from app.forms import TodoForm
from .models import todo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='tester')
def signout(request):
    logout(request)
    return redirect(login)

def test(request):
    
    if request.user.is_authenticated:
        user=request.user
        form=TodoForm()
        todos=todo.objects.filter(user=user).order_by('priority')

        return render(request,'index.html',context={'form':form,'todos':todos})
    else:
        return render(request,'index.html')

def login(request):
    logout(request)
    if(request.method=="GET"):
        form=AuthenticationForm
        context={
            'form':form
        }
        return render(request,'login.html',context=context)
    else:
        form=AuthenticationForm(data=request.POST)
        if(form.is_valid()):
            user=authenticate(username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
            if user is not None:
                loginUser(request,user)
                return redirect('tester')
            return HttpResponse('Authenticated')
        else:
            context={
            'form':form
            }
            return render(request,'login.html',context=context)

def signup(request):
    logout(request)
    if (request.method=="GET"):
        form=UserCreationForm()
        context={
            'form':form
        }
        return render(request,'signup.html',context=context)
    else:
        
        form=UserCreationForm(request.POST)
   
        if(form.is_valid()):
            user=form.save()
            print(user)
            if user is not None:
                return redirect('login')

        else:
     
            context={
            'form':form
            }
            return render(request,'signup.html',context=context)

@login_required(login_url='tester')
def addtodo(request):
    if request.user.is_authenticated:
        user=request.user
        print(user)
        form=TodoForm(request.POST)
        if(form.is_valid):
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('tester')
        else:
            context={
            'form':form
            }
            return render(request,'index.html',context=context)

@login_required(login_url='tester')
def deletetodo(request,id):
    todo.objects.get(pk=id).delete()
    return redirect('tester')

@login_required(login_url='tester')
def modtodo(request,id,status):
    print(id,'>',status)
    a=todo.objects.get(pk=id)
    a.status=status
    todo.save(a)
    return redirect('tester')
