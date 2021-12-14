# Script Purpose: Create a TCP Client
# Script Version: 1.0 
# Script Author:  Tala Vahedi

# Script Revision History:
# Version 1.0 Oct 6, 2021, Python 3.x

# import 3rd Party Modules
from __future__ import print_function

# import Python Standard Libraries
import socket       
import sys
import hashlib

# Psuedo Constants
SCRIPT_NAME    = "Script: Create a TCP Client"
SCRIPT_VERSION = "Version 1.0"
SCRIPT_AUTHOR  = "Author: Tala Vahedi"

if __name__ == '__main__':
    # Print Basic Script Information
    print()
    print(SCRIPT_NAME)
    print(SCRIPT_VERSION)
    print(SCRIPT_AUTHOR)
    print()  

    print("Client application starting up...")
    print("Establishing a connection on the same host using PORT 5555 \n")
    

    # 10 different messages to send to server
    messages = ['Hello World!','Cybersecurity is fun', 'University of Arizona', 'Cyber Operations', 'Python is great',
                'I love basketball', 'Cats are funny', 'Go wildcats', 'Happy Halloween', 'Going to the gym']

    # messages = ['Hello World!','Cybersecurity is fun']

    for message in messages:
        byteMessage = bytes(message, 'utf-8')
        # port Number of Server
        PORT = 5555        
        # create client socket
        clientSocket = socket.socket()
        # get my local host address
        localHost = socket.gethostname()
        # get my local host ip address range
        localIP = socket. gethostbyname(localHost)
        # connect to local address
        print("Attempt connection to: ", localIP, PORT)
        clientSocket.connect((localIP, PORT))
        print("Socket connected ...\n")  

        try:
            # sending message if there was a connection
            print("Sending the following message to server: ", byteMessage)
            clientSocket.sendall(byteMessage)
            print("Message sent\nReceiving message back from server...")
            hashedServerMessage = clientSocket.recv(1024)
            print("Server sent back an MD5 hash of message: ", hashedServerMessage, "\n")
            
        except Exception as err:
            sys.exit(err)