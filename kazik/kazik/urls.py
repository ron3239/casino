"""
URL configuration for kazik project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from kazik_index import views_1
from register_login import views

ajax_url=[
    path('permission',views_1.permission,name='permission'),
    path('win_lose',views_1.win_lose,name='win_lose'),
    path('update_balance',views_1.update_balance,name='update_balance'),
]




urlpatterns = [
    path('', views_1.index, name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    #game
    path('case/', views_1.case, name='case'), 
    path('ruletka/', views_1.ruletka, name='ruletka'),
    path('cards/', views_1.cards, name='cards'),
    path('ajax/', include(ajax_url)),  # Define AJAX patterns here
]

# !!
# неправильная адрессация
# !!

