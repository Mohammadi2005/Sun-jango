from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('log_in/', views.log_in, name='user_log_in'),
    path('log_out/', views.log_out, name='user_log_out'),
    path('register/', views.register, name='user_register'),
]