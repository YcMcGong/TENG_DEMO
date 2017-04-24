import socket
import sys

localhost = '143.215.111.5'
port = 12135
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (localhost, port)

def send_message(message):
    sent = sock.sendto(message.encode(), server_address)

def close_socket():
    print (sys.stderr, 'closing socket')
    sock.close()

send_message('double_tap')