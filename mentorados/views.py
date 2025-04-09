from django.shortcuts import render, redirect
from .models import Mentorados, Navigators, DisponibilidadeHorarios, Reuniao, Tarefa, Upload
from usuarios.views import login
from django.contrib.messages import constants
from django.contrib import messages
from datetime import datetime, timedelta
from .auth import valida_token
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def mentorados(request):

    '''if not request.user.is_authenticated:
        return redirect('login')'''

    if request.method == 'GET':
        navigators = Navigators.objects.filter(mentor=request.user)
        mentorados = Mentorados.objects.filter(mentor=request.user)

        '''
        estagios_flat = []
        for i in Mentorados.estagio_choices:
            print(i[1])
            estagios_flat.append(i[1])
        '''

        estagios_flat = [i[1] for i in Mentorados.estagio_choices]
        qtd_estagios = []
        for i, _ in Mentorados.estagio_choices:
            qtd_estagios.append(Mentorados.objects.filter(mentor=request.user, estagio=i).count())
            
            

        return render(request, 'mentorados.html', {'estagios': Mentorados.estagio_choices, 'navigators': navigators, 'mentorados': mentorados,'estagios_flat': estagios_flat, 'qtd_estagios': qtd_estagios})
    
       

    elif request.method == 'POST':
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')
        estagio = request.POST.get('estagio')
        navigator = request.POST.get('navigator')

    mentorado = Mentorados(
        nome=nome,
        foto=foto,
        estagio=estagio,
        navigator_id=navigator,
        mentor=request.user
        )
    mentorado.save()

    messages.add_message(request, constants.SUCCESS, 'Mentorado cadastrado com sucesso.')
    return redirect('mentorados')

@login_required
def reunioes(request):
    
    if request.method == 'GET':
        agendados = Reuniao.objects.filter(data__mentor=request.user, data__agendado=True)
        return render(request, 'reunioes.html', {'agendados': agendados})
    
    elif request.method =='POST':
        data =  request.POST.get('data')
        data = datetime.strptime(data, '%Y-%m-%dT%H:%M')

        disponiblidades = DisponibilidadeHorarios.objects.filter(mentor=request.user).filter(
            data_inicial__gte=(data - timedelta(minutes=50)),
            data_inicial__lte=(data + timedelta(minutes=50)),
            
        )

        if disponiblidades.exists():
            messages.add_message(request, constants.ERROR, 'Horário indisponível - Conflito de horários.')
            return redirect('reunioes')

        if data < datetime.now():
            messages.add_message(request, constants.ERROR, 'Data inválida.')
            return redirect('reunioes')

        disponibilidade = DisponibilidadeHorarios(
            data_inicial=data,
            mentor = request.user

        )
        disponibilidade.save()

        messages.add_message(request, constants.SUCCESS, 'Horário disponibilizado com sucesso.')
        return redirect('reunioes')


def auth(request):
    if request.method == 'GET':
        return render(request, 'auth_mentorado.html')
    elif request.method == 'POST':
        token = request.POST.get('token')

        if not Mentorados.objects.filter(token=token).exists():
            messages.add_message(request, constants.ERROR, 'Token inválido.')
            return redirect('auth_mentorado')
        
    response = redirect('escolher_dia')
    response.set_cookie('auth_token', token, max_age=3600)

    return response

def escolher_dia(request):

    if not valida_token(request.COOKIES.get('auth_token')):
        return redirect('auth_mentorado')

    if request.method == 'GET':
        mentorado = valida_token(request.COOKIES.get('auth_token'))

        disponibilidades = DisponibilidadeHorarios.objects.filter(
            data_inicial__gte = datetime.now(),
            agendado = False,
            mentor = mentorado.mentor
        ).values_list('data_inicial', flat=True)

        '''datas = []
        for disponibilidade in disponibilidades:
            datas.append(disponibilidade.date().strftime('%d-%m-%Y'))

        datas_dia_da_semana = []
        for disponibilidade in disponibilidades:
            datas_dia_da_semana.append(disponibilidade.strftime('%A'))

        datas_mes = []
        for disponibilidade in disponibilidades:
            datas_mes.append(disponibilidade.strftime('%B'))



        print(list((set((datas)))))
        print(list(set(datas_dia_da_semana)))
        print(list(set(datas_mes)))
'''

        datas_completas = [] #Lista para guardar a data e suas informacoes
        datas_unicas = set() #Set para guardar as datas unicas

        for disponibilidade in disponibilidades:
            data_formatada = disponibilidade.date().strftime('%d-%m-%Y')
            if data_formatada not in datas_unicas:
                datas_unicas.add(data_formatada)
                datas_completas.append({
                    'data': data_formatada,
                    'dia_da_semana': disponibilidade.strftime('%A'),
                    'mes': disponibilidade.strftime('%B'),
        })
                

        return render(request,'escolher_dia.html', {'datas': datas_completas}) 
    

def agendar_reuniao(request):

    if not valida_token(request.COOKIES.get('auth_token')):
            return redirect('auth_mentorado')
    
    mentorado = valida_token(request.COOKIES.get('auth_token'))

    if request.method == 'GET':
        data = request.GET.get('data')
        data = datetime.strptime(data, '%d-%m-%Y')
        
        horarios = DisponibilidadeHorarios.objects.filter(
            data_inicial__gte=data,
            data_inicial__lt=(data + timedelta(days=1)),
            agendado = False,
            mentor = mentorado.mentor

        )
        tags = Reuniao.tag_choices

        return render(request, 'agendar_reuniao.html', {'horarios': horarios, 'tags': tags})

    elif request.method == 'POST':

        tag = request.POST.get('tag')
        descricao = request.POST.get('descricao')
        horario_id = request.POST.get('horario')

        horario_real = DisponibilidadeHorarios.objects.get(id=horario_id)

        if horario_real.mentor != mentorado.mentor:
            messages.add_message(request, constants.ERROR, 'Horário não é do mesmo mentor do mentorado.')
            return redirect('escolher_dia')
        
        #ATOMICIDADE acid
        reuniao = Reuniao(
            data_id = horario_id,
            mentorado = mentorado,
            tag = tag,
            descricao = descricao
        )
        reuniao.save()

        horario = DisponibilidadeHorarios.objects.get(id=horario_id)
        horario.agendado = True
        horario.save()

        messages.add_message(request, constants.SUCCESS, 'Reunião agendada com sucesso.')
        return redirect('escolher_dia')

@login_required
def tarefa(request, id):
    mentorado = Mentorados.objects.get(id=id)
    if mentorado.mentor != request.user:
        raise Http404('Nao autorizado')

    if request.method == 'GET':
        tarefas = Tarefa.objects.filter(mentorado=mentorado)
        videos = Upload.objects.filter(mentorado=mentorado)

        return render(request,'tarefa.html', {'tarefas': tarefas, 'mentorado': mentorado, 'videos': videos})    

    elif request.method == 'POST':
        tarefa = request.POST.get('tarefa') 

        if not tarefa.strip():
            messages.add_message(request, constants.ERROR, 'Nenhuma tarefa cadastrada.')
            return redirect('tarefa', id=id)
        
        t = Tarefa(mentorado=mentorado, tarefa=tarefa)
        t.save()

        return redirect('tarefa', id=id)

def upload(request, id):
    mentorado = Mentorados.objects.get(id=id)
    if mentorado.mentor != request.user:
        raise Http404('Nao autorizado')

    if request.method == 'POST':
        video = request.FILES.get('video')
        upload = Upload(mentorado=mentorado, video=video)
        upload.save()

        return redirect('tarefa', id=id)
    
def tarefa_mentorado(request):
    mentorado = valida_token(request.COOKIES.get('auth_token'))
    if not mentorado:
        return redirect('auth_mentorado')
    
    if request.method == 'GET':
        tarefas = Tarefa.objects.filter(mentorado=mentorado)
        videos = Upload.objects.filter(mentorado=mentorado)

        return render(request, 'tarefa_mentorado.html', {'tarefas': tarefas, 'mentorado': mentorado, 'videos': videos})
       

@csrf_exempt
def tarefa_alterar(request, id):
    tarefa = Tarefa.objects.get(id=id)
    mentorado = tarefa.mentorado

    if mentorado.mentor != request.user or mentorado != valida_token(request.COOKIES.get('auth_token')):
        raise Http404('Nao autorizado')
    
    tarefa.realizada = not tarefa.realizada
    tarefa.save()
   
    return HttpResponse('teste')