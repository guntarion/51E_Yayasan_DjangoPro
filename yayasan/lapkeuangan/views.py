from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
from yayasan.institusi.models import Institusi
from yayasan.program.models import ProgramKerja
from yayasan.entitas.models import Entitas
from django.views import View

from .models import KodeAkun, JurnalTransaksi
from .forms import KodeAkunForm, JurnalTransaksiForm

import datetime

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
    # Fetch all JurnalTransaksi instances
    jurnal_transaksi_list = JurnalTransaksi.objects.all()
    context = {
        'parent': 'applications',
        'segment': 'jurnal_view',
        'jurnal_transaksi_list': jurnal_transaksi_list,  # Pass the instances to the template
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

class CreateEntryView(View):
    def get(self, request, *args, **kwargs):
        # Simulate user input
        user_input = {
            'nomer_transaksi': '123',
            'organisasi': 1,  # ID of the Institusi instance
            'entitas': 1,  # ID of the Entitas instance
            'urutan_transaksi': '1',
            'no_bukti_transaksi': '456',
            'program': 357,  # ID of the ProgramKerja instance
            'tanggal_transaksi': '2024-04-02',
            'kode_akun': 15,  # ID of the KodeAkun instance
            'nama_akun': 'Nama Akun dari kode akun',
            'keterangan': 'Test Keterangan',
            'jumlah': '100.00',
            'debet_or_kredit': 'debet',
            'nominal_debet': '50.00',
            'nominal_kredit': '50.00',
            'catatan': 'Test Catatan'
        }
        create_journal_entry(user_input)
        return HttpResponse('Entry created')


def generate_nomer_transaksi():
    # Get the current month in three-letter format
    current_month = datetime.datetime.now().strftime('%b').lower()

    # Get the latest JurnalTransaksi entry for the current month
    latest_entry = JurnalTransaksi.objects.filter(
        nomer_transaksi__startswith=current_month
    ).aggregate(Max('nomer_transaksi'))

    # Extract the number from the nomer_transaksi of the latest entry
    latest_number = int(latest_entry['nomer_transaksi__max'].split('-')[1]) if latest_entry['nomer_transaksi__max'] else 0

    # Increment the number by 1
    new_number = latest_number + 1

    # Create the nomer_transaksi for the new entry
    return f'{current_month}-{new_number:03}'

def generate_urutan_transaksi(kode_akun):
    # Get the current year and month in two-digit format
    current_year_month = datetime.datetime.now().strftime('%y%m')

    # Get the count of JurnalTransaksi entries for the current year, month, and kode_akun
    count = JurnalTransaksi.objects.filter(
        urutan_transaksi__startswith=f'{current_year_month}-{kode_akun.kode_akun}',
    ).count()

    # Increment the count by 1
    new_count = count + 1

    # Create the urutan_transaksi for the new entry
    return f'{current_year_month}-{kode_akun.kode_akun}-{new_count:03}'

def create_journal_entry(user_input):
    # Get the KodeAkun instance
    kode_akun = KodeAkun.objects.get(pk=user_input['kode_akun'])
    nama_akun = kode_akun.nama_akun

    # Generate nomer_transaksi and urutan_transaksi
    nomer_transaksi = generate_nomer_transaksi()
    urutan_transaksi = generate_urutan_transaksi(kode_akun)

    # Create a new JurnalTransaksi instance with the processed data
    jurnal_transaksi = JurnalTransaksi(
        nomer_transaksi=nomer_transaksi,
        organisasi=Institusi.objects.get(pk=user_input.get('organisasi')),
        entitas=Entitas.objects.get(pk=user_input.get('entitas')),
        urutan_transaksi=urutan_transaksi,
        no_bukti_transaksi=user_input.get('no_bukti_transaksi'),
        program=ProgramKerja.objects.get(pk=user_input.get('program')),
        tanggal_transaksi=user_input.get('tanggal_transaksi'),
        kode_akun=kode_akun,  
        nama_akun=nama_akun,
        keterangan=user_input.get('keterangan'),
        jumlah=user_input.get('jumlah'),
        debet_or_kredit=user_input.get('debet_or_kredit'),
        nominal_debet=user_input.get('nominal_debet'),
        nominal_kredit=user_input.get('nominal_kredit'),
        catatan=user_input.get('catatan')
    )
    jurnal_transaksi.save()