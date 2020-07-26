#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
serverPort = 5581
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
Sock.bind(('0.0.0.0',serverPort)) 
Sock.listen(5)
print ('The server is ready to receive') 
while 1:
    connectionSocket, addr = Sock.accept() 
    message = connectionSocket.recv(1024) 
    message = message.decode()
    modifiedmessage = message.lower() 
    connectionSocket.send(modifiedmessage.encode()) 
    connectionSocket.close()


# In[ ]:




