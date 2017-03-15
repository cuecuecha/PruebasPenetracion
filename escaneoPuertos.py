#!/usr/bin/python
#Script que analiza los puertos abiertos dado un dominio o ip

#Hernandez Cuecuecha Jorge Alberto
import socket
from socket import *

equipo = raw_input('ingresa el domino o ip que deseas escanear: ')
if(equipo==''):
  print"Es necesario agregar un dominio o ip"
  exit(0)
ports = raw_input('Ingresa el rango de puertos (1-100): ')
if(ports==''):
  print"Es necesario agregar un rango"
print '[+] Escaneando a %s en un rango de puertos %s ' % (equipo, ports)
separado = ports.split('-')
ipequipo = gethostbyname(equipo) #traducira lo ingresado
#Inicia el escaneo
print 'comenzando el escaneo en la ip ', ipequipo;
#creamos un ciclo con el rango
for puertos in range(int(separado[0]), int(separado[1]) +1):
  cliente = socket(AF_INET, SOCK_STREAM) #indicamos el socket
  resultado = cliente.connect_ex((ipequipo, puertos))
  if (resultado == 0):
    print 'puerto %d: Abierto' %(puertos)
  else:
    print 'puerto %d: Cerrado' %(puertos)
  cliente.close()#cerramos la conexion para que se analice el siguiente puerto