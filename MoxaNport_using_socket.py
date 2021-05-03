# Simple code for connecting NPORT Ethernet Serial converter using SOCKET module.
# Set NPORT to TCP Server and check IP address and Port in the code.
# Disable the Firewall if necessary.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.127.254', 4001)) #NPORT IP address and PORT

s.send(b'Testing Serial Connection')

s.close()
