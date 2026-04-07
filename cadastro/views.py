from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pessoa
from .forms import PessoaForm

def index(request):
    pessoas = Pessoa.objects.all()
    contexto = {
        'pessoas': pessoas,
    }
    return render(request, 'cadastro/index.html', contexto)

def contato(request):
    return render(request, 'cadastro/contato.html')

@login_required
def adicionar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pessoa adicionada com sucesso!')
            return redirect('index')
    else:
        form = PessoaForm()
    return render(request, 'cadastro/adicionar.html', {'form': form})

@login_required
def detalhe(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'cadastro/detalhe.html', {'pessoa': pessoa})

@login_required
def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pessoa atualizada com sucesso!')
            return redirect('detalhe', id=id)
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'cadastro/editar.html', {'form': form, 'pessoa': pessoa})

@login_required
def deletar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        pessoa.delete()
        messages.success(request, 'Pessoa deletada com sucesso!')
        return redirect('index')
    return render(request, 'cadastro/deletar.html', {'pessoa': pessoa})