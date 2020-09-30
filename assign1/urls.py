from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.register,name='assign1'),
    path('register',views.register,name='register')
]