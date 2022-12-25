from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required


from .models import Artikel, Kategori
from .forms import ArtikelForms

from myproject.forms import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ArtikelSerializer



@login_required
def dashboard(request):
    template_name = "back/dashboard.html"
    context = {
        'title' : 'dashboard'
    }
    return render(request, template_name, context)

@login_required
def artikel(request):
    user = User.objects.first()
    if request.user.groups.filter(name="operator").exists():
        user.has_perm('artikel.tambah_artikel')
        user.has_perm('artikel.edit_artikel')
        user.has_perm('artikel.hapus_artikel')
        user.has_perm('artikel.lihat_artikel')
        print("user adalah operator")
    else:
        print("user bukan opertaor")
    template_name = "back/tabel_artikel.html"
    artikel = Artikel.objects.all()
    print(artikel)  
    #for i in artikel: 
        #print(i.nama,'-',i.judul,'-',i.kategory)
    context = {
        'title' : 'Tabel Artikel',
        'artikel' : artikel,
    }
    return render(request, template_name, context)

@login_required
def tambah_artikel(request):
    template_name = "back/tambah_artikel.html"
    kategory = Kategori.objects.all()
    
    if request.method == "POST":
        forms_artikel = ArtikelForms(request.POST)
        if forms_artikel.is_valid():
            art = forms_artikel.save(commit=False)
            art.nama = request.user
            art.save()
            return redirect(artikel)
        
        return redirect(artikel)
    else:
        forms_artikel = ArtikelForms
    context = {
        'title' : 'Tambah Artikel',
        'kategory': kategory,
        'forms_artikel' : forms_artikel
    }
    return render(request, template_name, context)
    
@login_required
def lihat_artikel(request, id):
    template_name = "back/lihat_artikel.html"
    artikel = Artikel.objects.get(id=id)
    context = {
        'title' : 'lihat Artikel',
        'artikel':artikel,
    }
    return render(request, template_name, context)

@login_required
def edit_artikel(request, id):
    template_name = "back/tambah_artikel.html"
    a = Artikel.objects.get(id=id)
    if request.method == "POST":
        forms_artikel = ArtikelForms(request.POST, instance=a)
        if forms_artikel.is_valid():
            art = forms_artikel.save(commit=False)
            art.nama = str(a.nama)
            art.save()
            return redirect(artikel)
            
    else:
        forms_artikel = ArtikelForms(instance=a)
    
    context = {
        'title' : 'EDIT ARTIKEL',
        'artikel' :a,
        'forms_artikel':forms_artikel,
    }
    return render(request, template_name, context)

@login_required
def delete_artikel(request, id):
    Artikel.objects.get(id=id).delete()
    return redirect(artikel)

@staff_member_required
def users(request):
    template_name = "back/tabel_users.html"
    users = User.objects.all()
    context = {
        'title' : 'Tabel Users',
        'users' : users
    }
    return render(request, template_name, context)

@api_view(['GET'])
def artikel_list(request):
    list = Artikel.objects.all()
    serializer = ArtikelSerializer(list)
    return Response(serializer.data)
    

@api_view(['GET', 'PUT', 'DELETE'])
def artikel_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        artikel = Artikel.objects.get(pk=pk)
    except Artikel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtikelSerializer(artikel)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtikelSerializer(artikel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artikel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def lihat_users(request, id):
    template_name = "back/lihat_user.html"
    user = User.objects.get(id=id)
    print(user)
    context = {
        'title' : 'lihat Tabel User',
        'user' : user,
    }
    return render(request, template_name, context)

@login_required
def delete_users(request, id):
    User.objects.get(id=id).delete()
    return redirect(users)