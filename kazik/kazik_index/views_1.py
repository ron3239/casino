from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def index(request):
    context={
            'Login':'login'
    }

    return render(request=request,template_name='index.html')
@csrf_exempt
def case(request):
        return render (request,template_name='kazik_index\games\case.html')




# ajax
@csrf_exempt
def uptade_tokens(request):
    player = request.user

    if request.method == 'POST':
       data = {'tokens': player.token}

    return JsonResponse(data)



@csrf_exempt
def case_token_need(request):

        data={}

        if request.method == 'POST':

                tokens_need=request.POST.get('tokens_need')
                player=request.user

                if not player:
                       data={
                              'not_reg_log':True
                       }
                else:
                        tokens_user=int(player.token)
                        if tokens_user>=int(tokens_need):
                                data={
                                     'not_reg_log':False,
                                     'permission':True
                              }
                        else:
                                data={
                                     'not_reg_log':False,
                                     'permission':False
                              }

                return JsonResponse(data)
pass


@csrf_exempt
def win_lose(request):
    if request.method == 'POST':
        win = bool(int(request.POST.get('win')))
        need = int(request.POST.get('need'))
        player = request.user


        if win:
               player.token+=need
        elif player.token-need<0:
               player.token=0
        else:
               player.token-=need

        player.save()
        response_data = {'status': True}

        return JsonResponse(response_data)






