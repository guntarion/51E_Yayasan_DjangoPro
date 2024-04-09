from django.urls import path
from . import views
from .views import CreateEntryView

app_name = 'lapkeuangan'

urlpatterns = [
     path('autocomplete_program/', views.autocomplete_program,
         name='autocomplete_program'),
     path('autocomplete_entitas/', views.autocomplete_entitas,
         name='autocomplete_entitas'),
     path('autocomplete_akun/', views.autocomplete_akun,
          name='autocomplete_akun'),         
     path('get_unit_from_program/', views.get_unit_from_program,
         name='get_unit_from_program'),
     path('get_kode_akun/', views.get_kode_akun,
          name='get_kode_akun'),         

     path('kode_akun/', views.kode_akun_list_view, name='kode_akun_list'),
     path('kode_akun/new/', views.kode_akun_create_view, name='kode_akun_new'),
     path('kode_akun/<int:pk>/edit/', views.kode_akun_edit_view, name='kode_akun_edit'),
     path('jurnal/new/', views.jurnal_transaksi_create_view,
          name='jurnal_transaksi_new'),

     path('jurnal-view/', views.jurnal_view, name='jurnal_view'),
     path('labarugi-view/', views.labarugi_view, name='labarugi_view'),
     path('neraca-view/', views.neraca_view, name='neraca_view'),
     path('unitreport-view/', views.unitreport_view, name='unitreport_view'),

     path('create-entry/', CreateEntryView.as_view(), name='create-entry'),
]