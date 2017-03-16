#!/usr/bin/python
#Hernandez Cuecuecha Jorge Alberto
#
# Uso
#	python OsFingerprintingTCP.py 
 
import socket, sys
from struct import *

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error:
    print "Socket no creado"
    sys.exit(1)
 

packet = s.recvfrom(65565)#Se recibe el paquete
packet = packet[0]
ip_header = packet[0:20] #Obtenemos los primeros 20 caracteres de ip
#desempaquetamos
iph = unpack('!BBHHHBBH4s4s' , ip_header)
#obtenemos la version ip 
version_ihl = iph[0]
#igl
version = version_ihl >> 4
ihl = version_ihl & 0xF
iph_length = ihl * 4
ttl = iph[5]
#de esta forma sabemos que es TCP
protocol = iph[6]
s_addr = socket.inet_ntoa(iph[8]);
d_addr = socket.inet_ntoa(iph[9]);
 
print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
 
tcp_header = packet[iph_length:iph_length+20]
#Desempaqueta la cabecera
tcph = unpack('!HHLLBBHHH' , tcp_header)
source_port = tcph[0]
dest_port = tcph[1]
sequence = tcph[2]
acknowledgement = tcph[3]
doff_reserved = tcph[4]
tcph_length = doff_reserved >> 4
window = tcph[6]
print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port)
print "Tamanio Ventana: "+str(window)+"\n"
if(str(window)=="5840"):
	print("Sistema operativo Linux(Kernel 2.4 and 2.6")
elif(str(window)=="5720"):
	print("Sistema operativo Google Linux")
elif(str(window)=="65535"):
	print("Sistema Operativo FreeBSD Windows XP")
elif(str(window)=="8192"):
	print("Sistema Operativo Windows vista y 7")
elif(str(window)>"400" and str(window)<"550"):
	print("Sistema Operativo Kali Linux(kernel 4.6.0-kali1-amd64)")
else:
	print("No se reconoce el Sistema Operativo")