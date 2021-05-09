from django.shortcuts import render
from django.http import HttpResponse
devices = [
    {
        'name': 'PROD Server',
        'id': '1',
        'type': 'Server',
        'ip': '192.168.230.245',
        'mac': '24:EE:9A:F1:D7:AE',
        'info': 'Windows 2012 R2',
        'traffic': 'TX:2343 RX: 5498'
    },
    {
        'name': 'WAN Router',
        'id': '2',
        'type': 'Router',
        'ip': '192.178.100.254',
        'mac': '34:DD:8G:E1:D2:FD',
        'info': 'Cisco ISR 4432',
        'traffic': 'TX:4387 RX: 2343'
    }
]

# Create your views here.
def home(request):
    context = {
        'devices': devices
    }
    return render(request, 'netmon/home.html', context)

def about(request):
    return render(request, 'netmon/about.html', {'title': "About"})