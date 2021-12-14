# Script Purpose: Create a TCP Server
# Script Version: 1.0 
# Script Author:  Tala Vahedi

# Script Revision History:
# Version 1.0 Oct 5, 2021, Python 3.x

# 3rd Party Modules
from __future__ import print_function

import socket       # import Python Standard Socket Library
import sys
import hashlib

# Psuedo Constants
SCRIPT_NAME    = "Script: Create a TCP Server"
SCRIPT_VERSION = "Version 1.0"
SCRIPT_AUTHOR  = "Author: Tala Vahedi"

if __name__ == '__main__':
    # Print Basic Script Information
    print()
    print(SCRIPT_NAME)
    print(SCRIPT_VERSION)
    print(SCRIPT_AUTHOR)
    print()  

    print("TCP server starting up...\n\n")

    # create a socket
    sock = socket.socket()
    # get local host address
    localHost = socket.gethostname()  
    # get the local IP address range
    localIP = socket. gethostbyname(localHost)
    # specify the local port 
    localPort = 5555
    sock.bind((localIP, localPort))

    # program will continue until terminated by the user
    while True:
        # listen for incoming connections
        sock.listen(1)
        try:
            print('Waiting for a connection request...')
            # getting connection details
            connection, client = sock.accept()
            print("Connection received from client: ", client)
            # getting data message from client
            data = connection.recv(16)
            print("Client sent the  following message: ", data)
            # compute its md5 hash
            print("Creating an MD5 hash of message...")
            md5Hash = hashlib.md5(data).digest()
            # send the md5 hash back to client
            print("Sending MD5 hashed message back to client:", client)
            connection.sendall(md5Hash)
            print("Hashed MD5 message has been sent\n\n")
            
        # error in establishing a socket 
        except Exception as err:
            sys.exit(str(err))