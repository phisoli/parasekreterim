from django.urls import path
from .views import register, user_login, user_logout, add_money_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add_money/', add_money_view, name='add_money'),
]
