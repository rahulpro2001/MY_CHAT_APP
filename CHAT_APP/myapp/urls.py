from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.index,name='home'),
    path("<str:room>/",views.room,name = 'room'),
     path("checkview", views.checkview, name='checkview'),
     path("send",views.send,name="send"),
     path("getMessages/<str:room>/",views.getMessages,name = 'getMessages'),
]













