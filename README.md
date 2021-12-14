# TCP-Client-Server

The server.py file is a standalone Python Script that acts as a TCP Server. The Server accepts connections on Port 5555 from TCP Clients Operating on the same local IP range as the Server.  The server also receives a message, then creates an MD5 Hash of the Message and responds to the Client with the MD5 Digest generated.  The server continues to operate until terminated by the user.

The client.py file is a standalone Python Script that will act as a TCP Client.  The Client connects to the TCP Server Created in Assignment 10 on Port 5555.  The client also send 10 message to the Server with differing content and receives the hex digest response provided by the TCP Server. 
