#!/usr/bin/env python
# coding=utf-8
'''
class 2: lab2:
a. Write a script that connects using telnet to the pynet-rtr1 router. ExecuteÊhe 'show ip int brief' command on the router and return the output.
'''

import telnetlib
import time
import socket
import sys

# shared vars
TELNET_PORT = 23
TELNET_TIMEOUT = 6

ip_addr = '184.105.247.70'
uname = 'pyclass'
pwd = '88newclass'

COMMANDS = ["term len 0","sh ip int b","!!!end!!!\r\n"]

# Login function
def telnet_login(telnet_conn,uname,pwd):
    output = telnet_conn.read_until("sername",TELNET_TIMEOUT)
    telnet_conn.write(uname + '\n')
    output += telnet_conn.read_until("assword",TELNET_TIMEOUT)
    telnet_conn.write(pwd + '\n')

# Tetlnet function,create class obj for telnet connection
def telnet_func(ip_addr,TELNET_PORT,TELNET_TIMEOUT):
    try:
        return telnetlib.Telnet(ip_addr,TELNET_PORT,TELNET_TIMEOUT)
    except socket.timeout:# if socket timed out, exit
        print("Connection timed out")
        sys.exit()

# main function
def main():
    telnet_conn = telnet_func(ip_addr,TELNET_PORT,TELNET_TIMEOUT)
    telnet_login(telnet_conn,uname,pwd)
    # debug session
    #telnet_conn.set_debuglevel(1)

    time.sleep(1)
    for cmd in COMMANDS:
        telnet_conn.write(cmd+"\r\n")
    print(telnet_conn.read_until("!!!end!!!\r\n"))
    telnet_conn.close()

if __name__ == "__main__":
    main()
