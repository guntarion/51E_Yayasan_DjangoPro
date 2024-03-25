from django.shortcuts import render, redirect
from django.db.models import F
from .forms import ProgramKerjaForm
from .models import ProgramKerja

def render_yayasan(request, template_name, context=None, content_type=None, status=None, using=None):
    return render(request, f'yayasan/{template_name}', context, content_type, status, using)

def program_kerja_create_view(request):
    context = {
        'parent': 'pages',
        'sub_parent': 'users',
        'segment': 'reports',
        'form': ProgramKerjaForm(request.POST or None),
    }
    if context['form'].is_valid():
        context['form'].save()
        return redirect('/')
    return render_yayasan(request, 'program_kerja_create.html', context)



def program_kerja_list_view(request):
    programkerjas = ProgramKerja.objects.filter(tahun_anggaran=2024).annotate(
        jumlah=F('anggaran_januari') + F('anggaran_februari') + F('anggaran_maret') + 
        F('anggaran_april') + F('anggaran_mei') + F('anggaran_juni') + 
        F('anggaran_juli') + F('anggaran_agustus') + F('anggaran_september') + 
        F('anggaran_oktober') + F('anggaran_november') + F('anggaran_desember')
    ).select_related('owner_program')
    owners = ProgramKerja.objects.values_list('owner_program__namaUnit', flat=True).distinct()
    context = {
        'parent': 'applications',
        'segment': 'proker_list',
        'programkerjas': programkerjas,
        'owners': owners,
    }
    return render_yayasan(request, 'program_kerja_list.html', context)


# def program_kerja_list_view(request):
#     programkerjas = ProgramKerja.objects.all()
#     return render_yayasan(request, 'program_kerja_list.html', {'programkerjas': programkerjas})
