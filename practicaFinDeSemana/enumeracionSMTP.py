#!usr/bin/python
#Hernandez Cuecuecha Jorge Alberto
#
#	Modo de uso
#	python enumeracionSMTP.py ip
import socket
import sys
if len(sys.argv) != 2:
        sys.exit("python enumeracionSMTP.py ip")
ip= sys.argv[1]
comando = 'vrfy'
try:
	conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	conn.connect((ip,25))
	banner = conn.recv(1024)
	print banner

	if '220' in banner:
		with open('usuarios.txt','r') as us:
			#conn.sendall(comando+' '+str(us))
			for user in us:
				conn.send(comando+' '+user)
				result = conn.recv(1024)
				print result
				if '252' in result:
					print 'Usuario valido: ' + user
				if '550' in result:
					print 'Usuario invalido: ' + user 
	conn.close()
except socket.timeout:
	print 'timeout: '+ip
except socket.error:
	print 'timeout: '+ip