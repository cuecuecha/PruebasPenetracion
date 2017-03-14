#!usr/bin/python
#Hernandez Cuecuecha Jorge Alberto
#Script que recibe como parametro una ip o dominio y a traves de un ping
# este te dice con el parametro ttl el sistema operativo

#Uso python ping.py 8.8.8.8

import sys,subprocess
import os
if len(sys.argv) != 2:
        sys.exit("python ping.py ip")
ip=sys.argv[1]
command = "ping -c 1 " + ip
process = subprocess.check_output(command,shell=True)
#salida = process.communicate()
#print salida[0]
process = str(process.split('\n')[-6:])
#print process
lista=process.split("=")[2].split()
if(int(lista[0]=='128')|int(lista[0]=='127')):
	print "Sistema Operativo Windows"
elif(lista[0]=='64'):
	print "Linux 2.0.x Kernel, Solaris, Stratus, FreeBSD (2.1R,5), MacOS (10.5.6)"
elif(lista[0]=='254'):
	print "Cisco"
elif(lista[0]=='255'):
	print "Linux 24 kernel, NetBSD, Solaris"
elif(lista[0]=='60'):
	print "AIX, Irix, MacOS 2.0.x"
else:
	print "No se tiene registro"
