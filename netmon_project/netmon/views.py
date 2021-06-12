from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Device
from django.contrib.auth.mixins import LoginRequiredMixin

# devices = [
#     {
#         'dev_name': 'PROD Server',
#         'dev_id': '1',
#         'dev_type': 'Server',
#         'dev_ip': '192.168.230.245',
#         'dev_mac': '24:EE:9A:F1:D7:AE',
#         'dev_info': 'Windows Service 2012 R2',
#         'dev_tx_traffic': '2343',
#         'dev_rx_traffic': '2343',
#         'dev_last_updated': '2343',
#         'dev_added_by': '2343'
#     },
#     {
#         'dev_name': 'Router',
#         'dev_id': '2',
#         'dev_type': 'Router',
#         'dev_ip': '192.168.230.246',
#         'dev_mac': '24:EE:9A:F1:D7:AE',
#         'dev_info': 'Cisco ISR 4314',
#         'dev_tx_traffic': '3224',
#         'dev_rx_traffic': '3224',
#         'dev_last_updated': '2343',
#         'dev_added_by': '2343'
#     }
# ]

# Create your views here.
def home(request):
    context = {
        'devices': Device.objects.all()
    }
    return render(request, 'netmon/home.html', context)

class DeviceListView(LoginRequiredMixin, ListView):
    model = Device
    template_name = 'netmon/home.html'
    context_object_name = 'devices'

class DeviceDetailView(LoginRequiredMixin, DetailView):
    model = Device

class DeviceCreateView(LoginRequiredMixin, CreateView):
    model = Device
    fields = ['dev_name', 'dev_ip']

    def form_valid(self, form):
        form.instance.dev_added_by = self.request.user
        return super().form_valid(form)

class DeviceUpdateView(LoginRequiredMixin, DetailView):
    model = Device
    fields = ['dev_name', 'dev_ip']

    def form_valid(self, form):
        form.instance.dev_added_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        device = self.get_object()
        if self.request.user == device.author:
            return True
        return False

class DeviceDeleteView(LoginRequiredMixin, DetailView):
    model = Device
    success_url = '/'

    def test_func(self):
        device = self.get_object()
        if self.request.user == device.author:
            return True
        return False

def about(request):
    return render(request, 'netmon/about.html', {'title': "About"})