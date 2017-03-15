#!/usr/bin/python

#Hernandez Cuecuecha Jorge Alberto
	#Script que hace un escaneo de la red especificada para saber que host
	#estan arriba

	#Modo de uso
	#python netsweep.py
from datetime import datetime
from scapy.all import srp,Ether,ARP,conf
from netaddr import IPAddress
import netifaces as ni
try:
	##ip = raw_input("Ip para escanear (ip/mascara): ")
	ni.ifaddresses('eth0')
	ip=ni.ifaddresses('eth0')[2][0]['addr']
	netmask=ni.ifaddresses('eth0')[2][0]['netmask']
	bits = IPAddress(netmask).netmask_bits()
	ip = ip+"/"+str(bits)
	print "\n[*] Escaneado... "
	start_time = datetime.now()
	conf.verb = 0
	ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip),timeout=2)
	print "mAC - IP\n"
	i=0
	for snd,rcv in ans:
		print rcv.sprintf("Host %ARP.psrc%") #muestra los resultados
		i=1+i
	stop_time = datetime.now()
	total_time = stop_time - start_time
	print "\n[Escaneo completo]"
	print "Host up: " + str(i)
	print "Duracion: %s"%total_time

except KeyboardInterrupt:
	print "\nSaliendo"
	sys.exit(1)
