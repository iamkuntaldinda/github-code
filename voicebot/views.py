from django.shortcuts import render, redirect
from SDSaptorsheBoT import VoiceBot
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def covid19bot(request):
	return render(request,'voicebot.html')
def voicebot(request):
    voicebot = VoiceBot('KM3OLtX-o2tOxTjMbOxdHCIdz9NHy1xhux4iMXdsfrPP',
                        'https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/2c14d7ef-da2b-4c5e-a581-78aebb41e3f1',
                        '5421bf4f-5236-4ebe-8bf1-eb5c08ec82e8',
                        '5f40d3ff-1046-4f75-b5f7-dd32df11973f',
                        'ca0ddc0c-677f-46a4-900f-ca39a212ff00',
                        '2020-04-14')
    user_text = request.POST['user_data']
    print("text recieved - {}".format(user_text))
    res = voicebot.process(user_text)
    print("Language Code : ",res[1])
    params = {'bot_message':res[0],'language':res[1]}
    return render(request,'result.html',params)

def aboutus(request):
    return render(request,'about.html')
    
def contact(request):
    try:
        Name = request.POST['name']
        Email = request.POST['email']
        Phone = request.POST['phone']
        Message = request.POST['message']
        contact = Contact(name=Name,email=Email,phone=Phone,message=Message)
        contact.save()
        messages.success(request,'Message Recieved')
        return render(request,'about.html')
    except Exception as e:
        messages.error(request,e)
        return render(request,'about.html')
        
    