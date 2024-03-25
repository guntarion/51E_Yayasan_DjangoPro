from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import JsonResponse
from yayasan.program.models import ProgramKerja
from yayasan.entitas.models import Entitas

from .models import KodeAkun
from .forms import KodeAkunForm, JurnalTransaksiForm

def render_yayasan(request, template_name, context=None, content_type=None, status=None, using=None):
    return render(request, f'yayasan/{template_name}', context, content_type, status, using)


def kode_akun_list_view(request):
    kode_akun_list = KodeAkun.objects.all()
    context = {
        'parent': 'applications',
        'segment': 'kode_akun_list',
        'kode_akun_list': kode_akun_list,
    }
    return render_yayasan(request, 'kode_akun_list.html', context)

def kode_akun_create_view(request):
    if request.method == 'POST':
        form = KodeAkunForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kode_akun_list')
    else:
        form = KodeAkunForm()
    context = {
        'parent': 'applications',
        'segment': 'kode_akun_create',
        'form': form,
    }
    return render_yayasan(request, 'kode_akun_create.html', context)

def kode_akun_edit_view(request, pk):
    kode_akun = get_object_or_404(KodeAkun, pk=pk)
    if request.method == 'POST':
        form = KodeAkunForm(request.POST, instance=kode_akun)
        if form.is_valid():
            form.save()
            return redirect('lapkeuangan:kode_akun_list')
    else:
        form = KodeAkunForm(instance=kode_akun)
    context = {
        'parent': 'applications',
        'segment': 'kode_akun_edit',
        'form': form,
    }
    return render_yayasan(request, 'kode_akun_create.html', context)

def jurnal_transaksi_create_view(request):
    if request.method == 'POST':
        form = JurnalTransaksiForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/success/')
    else:
        form = JurnalTransaksiForm()
    context = {
        'parent': 'applications',
        'segment': 'jurnal_new',
        'form': form,
    }

    return render_yayasan(request, 'jurnal_new.html', context)

# Autocomplete for journal input
def autocomplete_program(request):
    if 'term' in request.GET:
        qs = ProgramKerja.objects.filter(
            nama_program__icontains=request.GET.get('term')
        )
        programs = list(qs.values_list('nama_program', flat=True))
        return JsonResponse(programs, safe=False)
    return render_yayasan(request, 'jurnal_new.html')

# def autocomplete_program(request):
#     if 'term' in request.GET and 'owner_program' in request.GET:
#         qs = ProgramKerja.objects.filter(
#             nama_program__icontains=request.GET.get('term')
#             owner_program_id=request.GET.get('owner_program')
#         )
#         programs = list(qs.values_list('nama_program', flat=True))
#         return JsonResponse(programs, safe=False)
#     return render_yayasan(request, 'jurnal_new.html')

def autocomplete_entitas(request):
    if 'term' in request.GET:
        qs = Entitas.objects.filter(
            nama_entitas__icontains=request.GET.get('term')
        )
        entitas = list(qs.values_list('nama_entitas', flat=True))
        return JsonResponse(entitas, safe=False)
    return render(request, 'jurnal_new.html')

def autocomplete_akun(request):
    if 'term' in request.GET:
        qs = KodeAkun.objects.filter(
            nama_akun__icontains=request.GET.get('term')
        )
        akuns = list(qs.values_list('nama_akun', flat=True))
        return JsonResponse(akuns, safe=False)
    return render(request, 'jurnal_new.html')



def jurnal_view(request):
    context = {
        'parent': 'applications',
        'segment': 'jurnal_view',
    }
    return render_yayasan(request, 'jurnal_view.html', context)

def labarugi_view(request):
    context = {
        'parent': 'applications',
        'segment': 'labarugi_view',
    }
    return render_yayasan(request, 'labarugi_view.html', context)

def neraca_view(request):
    context = {
        'parent': 'applications',
        'segment': 'neraca_view',
    }
    return render_yayasan(request, 'neraca_view.html', context)

def unitreport_view(request):
    context = {
        'parent': 'applications',
        'segment': 'unitreport_view',
    }
    return render_yayasan(request, 'unitreport_view.html', context)


# def get_unit_from_program(request):
#     if 'programName' in request.GET:
#         program = ProgramKerja.objects.filter(
#             nama_program=request.GET.get('programName')
#         ).first()
#         if program:
#             return JsonResponse({'unit': program.owner_program.namaUnit, 'kode_akun': program.kode_akun})
#     return JsonResponse({'error': 'Program not found'}, status=404)



def get_unit_from_program(request):
    if 'programName' in request.GET:
        program = ProgramKerja.objects.filter(
            nama_program=request.GET.get('programName')
        ).first()
        if program:
            try:
                kode_akun = KodeAkun.objects.get(kode_akun=program.kode_akun)
                return JsonResponse({'unit': program.owner_program.namaUnit, 'kode_akun': program.kode_akun, 'nama_akun': kode_akun.nama_akun, 'unit_id': program.owner_program.id, 'program_id': program.id, 'jenis_input_output': program.jenis_input_output})
            except ObjectDoesNotExist:
                return JsonResponse({'unit': program.owner_program.namaUnit, 'kode_akun': program.kode_akun, 'unit_id': program.owner_program.id})
    return JsonResponse({'error': 'Program not found'}, status=404)


def get_kode_akun(request):
    if 'nama_akun' in request.GET:
        try:
            akun = KodeAkun.objects.get(nama_akun=request.GET.get('nama_akun'))
            return JsonResponse({'kode_akun': akun.kode_akun})
        except KodeAkun.DoesNotExist:
            return JsonResponse({'error': 'KodeAkun with this nama_akun does not exist.'})
    return JsonResponse({'error': 'Invalid request.'})
