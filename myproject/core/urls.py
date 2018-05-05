from django.urls import path
from django.contrib.auth.views import login, logout
from .forms import LoginForm
from myproject.core import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('dashboard/', v.dashboard, name='dashboard'),
    path(
        'login/',
        login,
        {
            'template_name': 'login.html',
            'authentication_form': LoginForm},
        name='login'
    ),
    path('logout/', logout, name='logout'),
]
