from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ativo
from .forms import AtivoForm

@login_required
def ativo_list(request):
    ativos = Ativo.objects.all()
    return render(request, 'estoque/ativo_list.html', {'ativos': ativos})

@login_required
def ativo_create(request):
    if request.method == 'POST':
        form = AtivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ativo_list')
    else:
        form = AtivoForm()
    return render(request, 'estoque/ativo_form.html', {'form': form})

@login_required
def ativo_update(request, pk):
    ativo = get_object_or_404(Ativo, pk=pk)
    form = AtivoForm(request.POST or None, instance=ativo)
    if form.is_valid():
        form.save()
        return redirect('ativo_list')
    return render(request, 'estoque/ativo_form.html', {'form': form})

@login_required
def ativo_delete(request, pk):
    ativo = get_object_or_404(Ativo, pk=pk)
    if request.method == 'POST':
        ativo.delete()
        return redirect('ativo_list')
    return render(request, 'estoque/ativo_confirm_delete.html', {'ativo': ativo})
