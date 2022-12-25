from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('artikel/', artikel, name='tabel_artikel'),
    path('artikel/tambah', tambah_artikel, name='tambah_artikel'),
    path('artikel/lihat/<str:id>', lihat_artikel, name='lihat_artikel'),
    path('artikel/edit/<str:id>', edit_artikel, name='edit_artikel'),
    path('artikel/delete/<str:id>', delete_artikel, name='delete_artikel'),
    path('users/lihat/<str:id>', lihat_users, name='lihat_users'),
    path('users', users, name='tabel_users'),
    path('users/delete/<str:id>', delete_users, name='delete_users'),

    #api
    path('api/artikel/', artikel_list, name='artikel_list')
]

