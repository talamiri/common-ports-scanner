#! /usr/bin/python3
import socket
import time
import re
import sys
import pyfiglet

print('****************************************************************************')
intro = pyfiglet.figlet_format("Amitzi's Scanner")
print(intro)
print('This Port Scanner Was Written By Tal Amiri!')
print('If You Enter Invalid IP Address Run This Script Again!')
print('****************************************************************************')

#Target IP Validation
port_list = [20, 21, 22, 23, 53, 80, 110, 139, 443, 445, 3306]
target = input('Enter IP To Scan: ')
regexIP = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''


#This functions checks if the ip valid
def validateIP(target):
    while True:
        if (re.search(regexIP, target)):
            print('{} Is Being Scanned.'.format(target))
            return True

        else:
            print('{} Is invalid IP Address!'.format(target))
            print('Run This Script Again With A Valid IP Address!')
            return False

def scanner(port_list):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    for port in port_list:
        if s.connect_ex((target, port)):
            print('The port {} is closed!'.format(port))
        else:
            print('The port {} is open!'.format(port))



#Just main function sortage
def main():
    if validateIP(target) == True:
        start = time.time()
        scanner(port_list)
        end = time.time()
        print(f'Time taken {end - start:.2f} seconds')
    else:
        exit()
main()

