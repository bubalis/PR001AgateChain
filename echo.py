# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:57:23 2020

@author: benja
"""

from websocket import create_connection
ws = create_connection("ws://echo.websocket.org/")
print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()