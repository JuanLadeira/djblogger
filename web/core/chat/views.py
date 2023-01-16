from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "chat/index-chat.html",{} )
    

def room(request, room_name):
     return render(request, "chat/chatroom.html", { 'room_name': room_name })