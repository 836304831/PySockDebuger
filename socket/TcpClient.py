#-*- coding: utf-8 -*-
from log import logger
import socket
import threading

class TcpClient(threading.Thread):
    
    RECV_SIZE = 1024
    
    def __init__(self, sock, addr):
        threading.Thread.__init__(self)
        self.sock = sock
        self.ip, self.port = addr[0:]
    
    def sendall(self, data):
        if data is None:
            return False
        
        return self.sock.sendall(data) is None
        
    def run(self):
        if self.sock is None:
            return
        
        while 1:
            data = self.sock.recv(self.RECV_SIZE)
            if data == "":
                logger.error("socket closed")
                break
            
            logger.debug("data from %s:%d -> %s" % (self.ip, self.port, data))