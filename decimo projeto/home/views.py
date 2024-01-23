from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto
from django.contrib import messages

def index(request):
    dados_do_banco = Produto.objects.all()

    context = {
       'dados': dados_do_banco,
    }

    return render(request, 'home/index.html', context)

def contato(request):
  form = ContatoForm(request.POST) 
    
  if str(request.method) == 'POST':
    if form.is_valid():
      nome = form.cleaned_data['nome']
      email = form.cleaned_data['email']
      assunto = form.cleaned_data['assunto']
      mensagem = form.cleaned_data['mensagem']

      print('Mensagem enviada')
      print(f'Nome: { nome }')
      print(f'E-mail: { email }')
      print(f'Assunto: { assunto }')
      print(f'Mensagem: { mensagem }')

      messages.success(request, 'E-mail enviado com sucesso')
    else:
      messages.error(request, 'Erro. o email não foi enviado')

  context ={
       'form': form,
    }
        
  return render(request, 'home/contato.html', context)

def produtos(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao cadastrar produto')
    else:
        form = ProdutoModelForm()

    context = {
        'form': form
    }
    return render(request, 'home/produto.html', context)
