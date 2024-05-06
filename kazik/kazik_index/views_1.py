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
        return render (request,template_name='kazik_index\games\case.html')

@csrf_exempt
def ruletka(request):
       return render(request=request,template_name='kazik_index/games/ruletka.html')


# ajax
@csrf_exempt
def game_case(request):
       player = request.user
       if request.method== 'POST':
              if player.token>=5:
                     number=randint(0,2)
                     
                     if number == 1:
                            player.token+=2
                     elif number == 0:
                            player.token-=5
                            
                     player.save()
                     
                     data = {
                            'balance':player.token
                     }
              else:
                     data = {
                            'status':False
                            }
       return JsonResponse(data=data)
              
