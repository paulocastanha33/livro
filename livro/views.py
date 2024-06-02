from django.shortcuts import render, redirect, HttpResponse
from .models import Livro
from .forms import LivroForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def lista(request):
    dados = {
     'dados':Livro.objects.all()
    }
    return render(request, 'livro/lista.html', context=dados)

def detalhe(request, id_livro):
    dados = {
    'dados': Livro.objects.get(pk=id_livro)
    }
    return render(request, 'livro/detalhe.html', dados)

@login_required
def criar(request):
    if request.method == 'POST':
        livro_form = LivroForm(request.POST)
        if livro_form.is_valid():
            livro_form.save()
            messages.success(request, 'Livro criado com sucesso.')

             
        return redirect('lista')  
    else:  
        livro_form = LivroForm()
        formulario = {
            'formulario': livro_form
        }
        return render(request, 'livro/novo_livro.html',context=formulario)
    
@login_required
def editar(request, id_livro):
    livro = Livro.objects.get(pk=id_livro)   
    # novo_livro/1 -->GET
    if request.method == 'GET':
        formulario = LivroForm(instance=livro)
        return render(request,'livro/novo_livro.html',{'formulario': formulario}) 
    #caso requisição seja POST  
    else:
        formulario = LivroForm(request.POST, instance=livro)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Livro alterado com sucesso!')
            
        return redirect('lista')  
      
@login_required    
def excluir(request, id_livro):
    livro = Livro.objects.get(pk=id_livro)
    if request.method == 'POST':
        livro.delete()
        messages.warning(request, 'Livro excluido com sucesso!')
        return redirect('lista')
    return render(request, 'livro/confirmar_exclusao.html',{'item': livro})


