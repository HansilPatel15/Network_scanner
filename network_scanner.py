#!/usr/bin/env python

import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-t", "--target", dest="target", help="target ip address for network scan")
    #parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments)=parser.parse_args()
    if not options.target:
        print("[-] please specify an target , use --help for more info")
    # elif not options.new_mac:
    #     print("[-] please specify an MAC address , use --help for more info")
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #arp_request.show()
    broadcast = scapy.Ether(dst= "ff:ff:ff:ff:ff:ff")
    #broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    answered_list = scapy.srp(arp_request_broadcast , timeout = 1 ,verbose= False)[0]
    #print(answered_list.summary())

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
        #print(element[1].psrc + "\t\t"+ element[1].hwsrc)
       # print(element[1].hwsrc)
       # print('----------------------------------------------------------------------')

    return client_list

def print_result(result_list):
    print("IP\t\t\tMAC Address\n-------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_arguments()   #192.168.159.1/24
scan_result = scan(options.target)
print_result(scan_result)