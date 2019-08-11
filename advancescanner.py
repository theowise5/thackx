#!/usr/bin/python

from socket import *
import optparse
from threading import *

def connscan(tgtHost, tgtPorts):
        try:
                sock = socket(AF_INET, SOCK_STREAM)
                sock.connect((tgtHost,tgtPort))
                print '[+] %d/tcp Open ' % tgtPort 
        except:
                print '[-] %d/tcp Closed' % tgtPort
        finally:
                sock.closed()

def portscan(tgtHost, tgtPorts):
        try:
