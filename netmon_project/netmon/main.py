import platform
import subprocess
from django.db import models
from netmon.models import Device
from background_task import background

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

@background(schedule=10)
def start_monitor():
    devices = Device.objects.all()
    print(">>>>>>>>>>> In Start_monitor <<<<<<<<<<<")
    for device in devices:
        if (ping(device.dev_ip)):
            device.dev_status = "Alive"
        else:
            device.dev_status = "Dead"
        device.save(update_fields=["dev_status"])

if __name__ == '__main__':
    start_monitor()
