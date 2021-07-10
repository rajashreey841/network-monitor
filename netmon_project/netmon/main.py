import platform
import subprocess
from subprocess import PIPE, Popen
from getmac import get_mac_address
from getmac import getmac
from django.db import models
from netmon.models import Device
from background_task import background

# Global Variables
STATUS_STR_ALIVE = "Alive"
STATUS_STR_NOT_REACHABLE = "Not Reachable"

def icmp_ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    if(subprocess.call(command) == 0):
        return STATUS_STR_ALIVE
    
    return STATUS_STR_NOT_REACHABLE

def arp_mac_lookup(host):
    mac = getmac.get_mac_address(ip=str(host), network_request=True)
    print("host: ", str(host), "mac: ", mac)
    return str(mac)

@background(schedule=60)
def start_monitor():
    devices = Device.objects.all()
    print("\n>>>>>>>>>>> In Start_monitor <<<<<<<<<<<\n")
    for device in devices:
        # mac = arp_mac_lookup(arp_mac_lookup(device.dev_ip))
        # device.dev_mac = mac
        device.save(update_fields=["dev_mac"])
        icmp_status = icmp_ping(device.dev_ip)
        if (device.dev_status != icmp_status):
            device.dev_status = icmp_status
        device.save(update_fields=["dev_status"])

if __name__ == '__main__':
    start_monitor()
