from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from register_login.models import Player
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def user_login(request):
    logout(request)
    context = {'error_display_login': 'none'}
    if request.method == 'POST':
        username = request.POST.get('input_l_login')
        password = request.POST.get('input_l_password')

        player = authenticate(request, username=username, password=password)

        if player is not None:
            login(request, player)
            return redirect('home')
        else:
            context['error_display_login'] = 'block'

    return render(request, 'reg_log.html')




@csrf_exempt
def register(request):
    context = {'error_display': 'none'}
    if request.method == 'POST':
        try:
            username = request.POST.get('input_r_login')
            email = request.POST.get('input_r_email')
            password = request.POST.get('input_r_password')

            player = Player(username=username, email=email)
            player.set_password(password)  
            player.save()
            login(request, player)


            return redirect('home')
        except Exception as e:
            context = {'error_display': 'block'}
    return render(request, 'reg_log.html')