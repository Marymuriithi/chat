from django.urls import path

from chats.views import index

app_name = 'chats'

urlpatterns = [

    path('', index, name= 'index'),
]