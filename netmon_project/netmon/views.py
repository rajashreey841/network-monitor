from django.shortcuts import render
from django.http import HttpResponse
devices = [
    {
        'dev_name': 'PROD Server',
        'dev_id': '1',
        'dev_type': 'Server',
        'dev_ip': '192.168.230.245',
        'dev_mac': '24:EE:9A:F1:D7:AE',
        'dev_info': 'Windows Service 2012 R2',
        'dev_tx_traffic': '2343',
        'dev_rx_traffic': '2343',
        'dev_last_updated': '2343',
        'dev_added_by': '2343'
    },
    {
        'dev_name': 'Router',
        'dev_id': '2',
        'dev_type': 'Router',
        'dev_ip': '192.168.230.246',
        'dev_mac': '24:EE:9A:F1:D7:AE',
        'dev_info': 'Cisco ISR 4314',
        'dev_tx_traffic': '3224',
        'dev_rx_traffic': '3224',
        'dev_last_updated': '2343',
        'dev_added_by': '2343'
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