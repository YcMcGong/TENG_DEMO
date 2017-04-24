import socket
import sys
import RPi.GPIO as GPIO

localhost = '143.215.111.5'
port = 12135
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = (localhost, port)
sock.bind(server_address)

def light_up():
    print('light up')
    pass

def light_off():
    print('light off')
    pass

while True:
    data, address = sock.recvfrom(4096)
    
    print(data)
    if(data == 'double_tap'): light_up()
    elif(data == 'long_blow'): light_off()

