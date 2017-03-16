#!/usr/bin/lua
--Hernández Cuecuecha Jorge Alberto
--Requerimientos
--	apt-get install luarocks 
--	apt-get install lua-socket
-- Uso
--	lua5.3 enumeracion.lua
local socket = require("socket")
print("Ingresa la ip: ")
local ip = io.read()
local client = socket.connect(ip,25)
if client then
	print ('Conectaddo')
else 
	print('offline')
	os.exit()
end
local msg = client:receive()
print(msg)
if string.match(msg, "220") == "220" then
	print("Ingresa el Usuario: ")
	local us = io.read()
	result = ""
	client:send("vrfy "..us.."\n")
	result = result ..client:receive()
	print(result)
	if string.match(result, "252") == "252" then
		print("Usuario valido: "..us)
	else
		print("Usuario invalido: "..us)
	end
end

