#!/usr/bin/env python3
from ipaddress import ip_address, IPv4Address, IPv6Address


userinput = input("Please enter an IPv4 address: ")

try:
    print(ip_address(userinput)) 
    ip = userinput.rsplit(".")
    if len(ip) == 4:
        print("it's an IPv4 address!!")
    else:
        print("That's not an IPv4 address!!")
        userinput = input("Try again")

except:
    print("That's not an IP address!!")

