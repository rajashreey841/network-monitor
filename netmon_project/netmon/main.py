import os
import platform
import subprocess
import json
import datetime
import secrets
from subprocess import PIPE, Popen
from getmac import get_mac_address
from getmac import getmac
from django.db import models
from django.contrib.auth.models import User
from netmon.models import Device
from background_task import background
# Emails
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Global Variables
STATUS_STR_ALIVE = "Alive"
STATUS_STR_NOT_REACHABLE = "Not Reachable"
GUI_ALERT_ALIVE = "Alive"
GUI_ALERT_NOT_REACHABLE = "Not Reachable"
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_ALERT_SUBJECT = "<< Network Monitor Alert >>"
EMAIL_ALERT_BODY = ",\n\tThis is to inform you that the following device has become unreachable."

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

def lldp_data_population(device):
    f = open("lldp.json",)
    data = json.load(f)
    if(device.dev_mac and device.dev_mac != "None"):
        return
    device.dev_mac = secrets.choice(data["l2fwdaddr"])
    print(secrets.choice(data["l2fwdaddr"]))
    device.save(update_fields=["dev_mac"])
    snmp_traffic_stats(device)
    return

def snmp_traffic_stats(device):
    return

def email_form_message(user_name, dev_name, dev_ip):
    return "Attention " + str(user_name) + EMAIL_ALERT_BODY + "\n" + str(dev_name) + "(" + dev_ip + ")"


def email_send_alert(dev_name, dev_ip):
    users = User.objects.all()
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    for user in users:
        msg = MIMEMultipart()
        msg['From']=EMAIL_HOST_USER
        msg['To']=user.email
        msg['Subject']=EMAIL_ALERT_SUBJECT
        message = email_form_message(user.username, dev_name, dev_ip)
        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        del msg
    return

@background(schedule=60)
def start_monitor():
    devices = Device.objects.all()
    print("\n>>>>>>>>>>> In Start_monitor <<<<<<<<<<<\n")
    for device in devices:
        lldp_data_population(device)
        icmp_status = icmp_ping(device.dev_ip)
        if (device.dev_status != icmp_status):
            device.dev_status = icmp_status
            # if (icmp_status == STATUS_STR_NOT_REACHABLE):
                # email_send_alert(device.dev_name, device.dev_ip)
        device.save(update_fields=["dev_status"])
        device.dev_last_updated = f"{datetime.datetime.now():%d.%m.%Y %H:%M:%S}"
        device.save(update_fields=["dev_last_updated"])
    print("\n>>>>>>>>>>> Complete <<<<<<<<<<<\n")
    return

if __name__ == '__main__':
    start_monitor()