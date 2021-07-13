from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Device(models.Model):
    dev_name = models.CharField(max_length=100)
    dev_id = models.IntegerField
    dev_type = models.CharField(max_length=100)
    dev_ip = models.CharField(max_length=16)
    dev_mac = models.CharField(max_length=18)
    dev_info = models.CharField(max_length=100)
    dev_tx_traffic = models.IntegerField(max_length=100, default="456987")
    dev_rx_traffic = models.IntegerField(max_length=100, default="387654")
    dev_last_updated = models.CharField(max_length=100)
    dev_added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    dev_status = models.CharField(max_length=20, default="Alive")
    dev_status_changed = models.IntegerField(max_length=1, default="0")
    dev_latency = models.DecimalField(max_digits=40, decimal_places=40, default="0.0")
    dev_latency_count = models.IntegerField(max_length=4, default="0")

    def __str__(self):
        return self.dev_name
    
    def get_absolute_url(self):
        return reverse('device-detail', kwargs={'pk': self.pk})
