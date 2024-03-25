# urls.py
from django.urls import path
from .views import program_kerja_create_view, program_kerja_list_view

app_name = 'program'

urlpatterns = [
    path('', program_kerja_list_view, name='program_kerja_list'),
    path('new/', program_kerja_create_view, name='program_kerja_new'),
]