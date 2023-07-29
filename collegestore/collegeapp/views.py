from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .models import Department, FormData, Course


def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('department')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']  # Correct the key to 'email'
        password = request.POST['password']
        confirm_password = request.POST['password1']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username is already registered. Please choose a different username.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email is already registered. Please use a different email address.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save()
                messages.info(request, 'Registration completed')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match. Please try again.')
            return redirect('register')

    return render(request, "register.html")

def details(request):
    return render(request,'details.html')

def department(request):
    return render(request,'department.html')

def confirmation(request):
    return render(request, 'confirmation.html')

# class FormDataListView(ListView):
#     model = FormData
#     form_class = Formdataform
#     context_object_name = 'form_data_list'
#     template_name = 'details.html'
# class FormDataCreateView(CreateView):
#     model = FormData
#     form_class = Formdataform
#     success_url = reverse_lazy('listview')
#     template_name = 'formdataform.html'
#
# class FormDataUpdateView(UpdateView):
#     model = FormData
#     form_class = Formdataform
#     success_url = reverse_lazy('listview')
#
#
#
# def department (request):
#     department_id=request.GET.get('department')
#     courses=Course.objects.filter(department_id=department_id).order_by('name')
#     return render(request, 'department.html', { 'courses': courses})
