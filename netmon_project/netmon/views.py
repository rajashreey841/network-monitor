from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Device

def home(request):
    context = {
        'devices': Device.objects.all()
    }
    return render(request, 'netmon/home.html', context)

class DeviceListView(LoginRequiredMixin, ListView):
    model = Device
    template_name = 'netmon/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'devices'
    ordering = ['-dev_last_updated']

class DeviceDetailView(LoginRequiredMixin, DetailView):
    model = Device

class DeviceCreateView(LoginRequiredMixin, CreateView):
    model = Device
    fields = ['dev_name', 'dev_ip']

    def form_valid(self, form):
        form.instance.dev_added_by = self.request.user
        return super().form_valid(form)

class DeviceUpdateView(LoginRequiredMixin, UpdateView):
    model = Device
    fields = ['dev_name', 'dev_ip']

    def form_valid(self, form):
        form.instance.dev_added_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        device = self.get_object()
        if self.request.user == device.dev_added_by:
            return True
        return False

class DeviceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Device
    success_url = '/'

    def test_func(self):
        device = self.get_object()
        if self.request.user == device.dev_added_by:
            return True
        return False

def about(request):
    return render(request, 'netmon/about.html', {'title': "About"})