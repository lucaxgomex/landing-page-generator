from django.shortcuts import render, redirect
from .models import Aluno
from .forms import AlunoForm

def home(request):
    # traz todo mundo do banco de dados
    alunos = Aluno.objects.all()
    dados = {
        'alunos': alunos
    }
    return render(request, 'home.html', dados)

def cadastro(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            try:
                instancia = form.save(commit=False)
                instancia.save() # salvamento no banco
                # return redirect('home')
            except:
                #print(request, "Erro ao cadastrar a produto!")
                print('Erro ao cadastrar')
    form = AlunoForm()
    dados = {
        'form': form
    }
    return render(request, "cadastro.html", dados)

def editar(request, id):
    aluno = Aluno.objects.get(id = id)
    if request.method == 'POST':
        if aluno:
            form = AlunoForm(request.POST, instance=aluno)
        else:
            form = AlunoForm(request.POST)

        if form.is_valid():
            try:
                instancia = form.save(commit=False)
                instancia.save() # salvamento no banco
                # return redirect('home')
            except:
                #print(request, "Erro ao cadastrar a produto!")
                print('Erro ao editar')    
        dados = {
            "form": form
        }
        return redirect('editar', id = aluno.id)
    else:
        if aluno:
            form = AlunoForm(instance=aluno)            
        else:
            form = AlunoForm()            
        dados = {
            "form": form
        }    
        return render(request, 'editar.html', dados)

def excluir(request, id):
    aluno = Aluno.objects.get(id = id)
    if aluno:
        aluno.delete()
        return redirect('home')
    else:
        print('Aluno nao encontrado')
        return redirect('home')