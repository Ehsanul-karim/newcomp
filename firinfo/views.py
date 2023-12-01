from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from myapp.models import CASE_FIR, witnessInfo, victimInfo, PhysicalStructure, AdminProfile

# Create your views here.
def firinfo(request,fir_id,admin_id):
    admin_info = get_object_or_404(AdminProfile, id=admin_id)
    case_info = CASE_FIR.objects.get(id=fir_id)
    witness_infos = witnessInfo.objects.filter(fir_id=case_info)
    victim_infos = victimInfo.objects.get(id=case_info.victim_name.id)
    physical_structure_infos = PhysicalStructure.objects.get(fir_id=case_info)

    print(case_info)
    print(victim_infos)
    print(f'printing victims id{victim_infos.id}')
    print(physical_structure_infos)
    print(witness_infos)
    return render(request, 'firinfo.html', {'user':admin_info, 'case_info' : case_info,'witness_infos':witness_infos,'victim_infos':victim_infos,'physical_structure_infos':physical_structure_infos })

def applyfir(request, user_id):
    return render(request, 'applyfir.html', {'user_id': user_id})