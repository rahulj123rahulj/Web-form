from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('assign-1/',include('assign1.urls')),
    path('assign-2/',include('assign2.urls')),
]