from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import render
from salespipeline.models import Salespipeline, SalespipelineForm

def index(request):
    return HttpResponseRedirect(reverse('salespipeline:search'))

def search(request):
    list = Salespipeline.objects.all()
    params = { 'list' : list }
    return render(request, 'salespipeline/search.html', params)

def edit(request, salespipeline_id):
    salespipelineForm = SalespipelineForm()
    if salespipeline_id > 0:
        salespipeline = Salespipeline.objects.get(salespipeline_id=salespipeline_id)
        salespipelineForm = SalespipelineForm(instance=salespipeline)

    params = {
        'salespipeline_id' : salespipeline_id,
        'form' : salespipelineForm
    }
    return render(request, 'salespipeline/edit.html', params)

def regist(request):
    salespipeline_id = request.POST.get('salespipeline_id')
    salespipeline = Salespipeline()
    if int(salespipeline_id) > 0:
        salespipeline = Salespipeline.objects.get(salespipeline_id=salespipeline_id)
    salespipelineForm = SalespipelineForm(request.POST, instance=salespipeline)
    if salespipelineForm.is_valid():
        salespipelineForm.save()
        return HttpResponseRedirect(reverse('salespipeline:search'))
    else:
        salespipeline_id = request.POST.get('salespipeline_id')
        params = {
            'salespipeline_id' : salespipeline_id,
            'form' : salespipelineForm,
        }
        return render(request, 'salespipeline/edit.html', params)