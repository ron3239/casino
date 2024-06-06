import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from random import randint



@csrf_exempt
def index(request):
    context={
            'Login':'login'
    }

    return render(request=request,template_name='index.html')
@csrf_exempt
def case(request):
        return render (request,template_name='kazik_index/games/case.html')

@csrf_exempt
def ruletka(request):
       return render(request=request,template_name='kazik_index/games/ruletka.html')

@csrf_exempt
def cards(request):
       return render(request=request,template_name='kazik_index/games/cards.html')


# ajax
@csrf_exempt
def win_lose(request):
    if request.method == 'POST':
        player = request.user
        
        win = int(request.POST.get('win'))
        kol = int(request.POST.get('kol'))
        if win==1:
            player.token += kol
        elif win==0:
            player.token -= kol
        player.save()
        return JsonResponse({'message': 'Success'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

#переделать


@csrf_exempt 
def permission(request):
    player = request.user
    if request.method == 'POST':
        date = request.POST.get('tokens')
        if date:
            if player.token >= int(date): # Проверяем количество токенов
                return JsonResponse({
                    'permission': True
                })

            else:
                return JsonResponse({
                    'permission': False
                })
    pass


@csrf_exempt
def update_balance(request):
       player=request.user
       if request.method=="POST":
              return JsonResponse({'tokens':player.token})