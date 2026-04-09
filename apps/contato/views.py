from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm


def contato(request):
    form = ContatoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Mensagem enviada com sucesso! Obrigado pelo contato.')
        return redirect('contato')

    return render(request, 'contato/index.html', {'form': form})
