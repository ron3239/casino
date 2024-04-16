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
from django.urls import path
from kazik_index import views_1
from register_login import views

urlpatterns = [
    path('',views_1.index,name='home'),
    path('admin/', admin.site.urls),
    path('login/',views.user_login,name='login'),
    path('register/', views.register, name='register'),
    path('case/',views_1.case,name='case'),
    # ajax
    path('game_case/',views_1.game_case,name='game_case'),
]


