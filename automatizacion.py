#!usr/bin/python
#Hernandez Cuecuecha Jorge Alberto
#Script que realiza una transferencia de zona, ingresando como argumento
# un dominio

#Referencia: https://github.com/rbsec/dnscan/blob/master/dnscan.py
import sys,os,subprocess
try:
	import dns.query
	import dns.resolver
	import dns.zone
except:
	print("Modulo dnspython no esta")
	sys.exit(1)
if len(sys.argv) != 2:
	sys.exit("python automatizacion.py dominio")

dominio=sys.argv[1]
#dominio="ole.com.ar"
ns= dns.resolver.query(dominio,"NS") #busca NS
for datos in ns: #ciclo for para que pruebe cada NS
	try:
		print("analizando "+str(datos)+"\n")
		command = "dig @"+str(datos)+ " axfr "+ dominio
		print subprocess.check_output(command,shell=True)
	except:
		print "Error en la transferencia de zona"


