from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from . import forms
from django.contrib import messages

import requests

from blog.models import Artikel


def index(request):
    template_name = 'front/index.html'
    data = True
    result = None
    Total = None
    Tanggal = None
    while(data):
        try:
            result = requests.get('https://data.covid19.go.id/public/api/update.json')
            Total = result.json()['update']['total']
            Tanggal = result.json()['update']['penambahan']['tanggal']
            data = False
        except:
            data = True
    context = {
        'title':'halaman index',
        'Total' : Total,
        'Tanggal' : Tanggal,

    }
    return render(request, template_name, context)

def detail_artikel(request, id):
    template_name = 'front/detail_artikel.html'
    artikel = Artikel.objects.get(id=id)
    context = {
        'title' : 'halaman detail artikel',
        'artikel' :artikel
    }
    return render(request,template_name, context)

def about(request):
    template_name = 'front/about.html'
    context = {
        'title' : 'halaman about'
    }
    return render(request, template_name, context)

def blog(request):
    template_name = 'front/blog.html'
    artikel = Artikel.objects.all()
    print(artikel)
    context = {
        'title' : 'halaman blog',
        'artikel' : artikel,
    }
    return render(request, template_name, context)

def statistik(request):
    template_name = 'front/covid.html'

    data = True
    data_provinsi = True

    result = None
    result_provinsi = None

    Total = None
    Provinsi = None
    Tanggal = None
    Tanggal_Provinsi = None
    
    while(data):
        try:
            result = requests.get('https://data.covid19.go.id/public/api/update.json')       

            Total = result.json()['update']['total']    
            Tanggal = result.json()['update']['penambahan']['tanggal']   

            data = False  
            
        except:
            data = True
            

    while(data_provinsi):
        try:
            result_provinsi = requests.get('https://data.covid19.go.id/public/api/prov.json')

            Provinsi = result_provinsi.json()['list_data']
            Tanggal_Provinsi = result_provinsi.json()['last_date']

            data_provinsi = False

        except:
            data_provinsi = True
            

    context = {
        'title' : 'halaman data covid',
        'Total' : Total,
        'Provinsi' : Provinsi,
        'Tanggal' : Tanggal,
        'Tanggal_Provinsi' : Tanggal_Provinsi,
        
    }
    return render(request, template_name, context)

def login(request):
    if request.user.is_authenticated:
        print('Sudah Login')
        return redirect ('index')
    template_name = "account/login.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #data ada
            print('username benar')
            auth_login(request, user)
            return redirect('index')
        else:
            #data tidak ada
            print('username salah')
            

    context = {
        'title' : 'Form Login',
    }
    return render(request, template_name, context)

#def register(request):
    #template_name = "account/register.html"

    #if request.method == "POST":
      #  form = NewUserForm(request.POST)
      #  if form.is_valid():
      #      user = form.save()
      #      login(request, user)
      #      messages.success(request, "Registrasi Berhasil." )
      #      return redirect('index')
       # messages.error(request, "Registrasi Tidak Berhasil. Invalid Informasi.")
    #form = NewUserForm()

   # context = {
    #    'title' : 'Form Register',
      #  'register_form' : form
  #  }
   # return render(request, template_name, context)

def register(request):
    template_name = 'account/register.html'
    form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if request.POST.get('password1') == request.POST.get('password2'):
            if form.is_valid():
                user_new = form.save()
                messages.success(request, "Terimakasih Telah Registrasi, Sekarang Anda Telah Login.")
                return redirect('index')
        else:
            return redirect('register')

    context = {
        'title' : 'Form Register',
        'form':form
    }
    return render(request, template_name, context)
                


def logout_view(request):
    logout(request)
    return redirect ('index')

