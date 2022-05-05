
# ITS A LAB THAT WILL TECH AXOSOLAMAN OS COMAND USEING PYTHON

import os

import shlex

print("LEST EXECUTE OS COMAND USEING PYTHON")

#tes = os.system("whoami")
#name = input("your name\n")
#comand = os.system("echo you are " + name)
#print(comand)

print("COMAND THAT WILL RUN \n traceroute -I $IP ")
#ip =input("Enter IP\n")
ip =shlex.quote(input("Enter IP\n"))
#ip =shlex.split(input("Enter IP\n"))
#print(ip)

comand = os.system("sudo traceroute -I " + ip )

print(comand)








