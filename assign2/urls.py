from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.messages,name='assign2'),
    path('messages',views.messages,name="messages"),
    path('show',views.show,name="show"),
]