#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import sys
import socket

# Constantes. Dirección IP del servidor y contenido a enviar
try:
    SERVER = str(sys.argv[1])
    PORT = int(sys.argv[2])
    METOD = sys.argv[3]
    ADRESS = sys.argv[4]
    TIME = sys.argv[5]

except (IndexError, ValueError):
    print("Usage: client.py ip puerto register sip_address expires_value")

if METOD == 'register':
    LINE = ('sip:' + ADRESS + "SIP/2.0\r\n\r\n" + 'expire_time:' + TIME + '\r\n\r\n')

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", LINE, end='')
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'), end='')

print("Socket terminado.")
