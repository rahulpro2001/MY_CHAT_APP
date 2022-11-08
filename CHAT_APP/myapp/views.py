from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from myapp.models import Room, Message

# Create your views here.
def index(request):
    return render(request,"index.html")

def room(request,room):
    username = request.GET.get('username') 
    room_det = Room.objects.get(name=room)   
    context={
        "username":username,
        "room_name":room,
        "room_det" : room_det
    }
    return render(request,"room.html",context)


def checkview(request):
    temp_room = request.POST['roomname'],
    username = request.POST['username']
    room=""
    for a in temp_room:
        room+=a
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name = room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)



def send(request):
    user_name = request.POST['username']
    room_id = request.POST['room_id']
    message = request.POST['message']
    new_message = Message.objects.create(value = message, room = int(room_id), user = user_name)
    new_message.save()
    return HttpResponse("success")

#where we are using this get we passs req and room name
def getMessages(request,room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room = room_details.id).values()
    return JsonResponse({"messages":list(messages)})