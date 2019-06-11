#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""
import sys
import json
import time
import socketserver

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """Echo server class."""

    dicc_registers = {}

    def register2json(self):
        """Convertir a json."""
        json.dump(self.dicc_registers, open('registed.json', 'w'), indent=3)

    def json2registered(self):
        """Si existe file_json lo pasa a mi diccionario."""
        try:
            with open('registed.json', 'r') as file_json:
                self.dicc_registers = json.load(file_json)
        except FileNotFoundError:
            pass

    """ Comprobar si un usuario está caducado """
    def expires(self):
        i = 1
        while n <= len(self.diclient):
            for user in self.diclient:
                now = time.ctime(time.time())
                if self.diclient[user][1] <= now:
                    del self.diclient[user]
                    break
            i = i + 1

  def handle(self):
        """Handle method of the server."""
        if self.dic_clients == {}:
            self.json2register()
        self.wfile.write(b"Hemos recibido tu peticion ")
        for line in self.rfile:
            informacion = line.decode('utf-8').split(" ")
         if (informacion[0] == "REGISTER"):
                user = informacion[1].split(':')[1]
                self.dicc_registers[user] = [IP]
                self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            elif (informacion[0] == "EXPIRES:"):
                TIME = informacion[1].split(':')[-1]
                then = time.strftime(
                        '%Y-%m-%d %H:%M:%S', time.gmtime(
                                time.time() + float((expires))))
                self.dic_clients[sip_address]["expires"] = then
                if expires == '0':
                    del self.dic_clients[sip_address]
                else:
                    self.expires()
        print("Nuevo usuario registrado")
        self.register2json()

if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the SIPRegisterHandler class to manage the request
    try:
        serv = socketserver.UDPServer(('',int(sys.argv[1])), SIPRegisterHandler)
        print("Lanzando servidor UDP de eco...")
        try:
            serv.serve_forever()
        except KeyboardInterrupt:
            print("Finalizado servidor")
    except (IndexError, ValueError, PermissionError):
        print("Usage: phython3 server.py puerto")
