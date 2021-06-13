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
    dev_tx_traffic = models.IntegerField(max_length=100, default="987642")
    dev_rx_traffic = models.IntegerField(max_length=100, default="456787")
    dev_last_updated = models.DateTimeField(default=timezone.now)
    dev_added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    dev_status = models.CharField(max_length=5, default="Alive")

    def __str__(self):
        return self.dev_name
    
    def get_absolute_url(self):
        return reverse('device-detail', kwargs={'pk': self.pk})