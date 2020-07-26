#!/usr/bin/env python
# coding: utf-8

# In[5]:


import socket
serverName = socket.gethostname()#'192.168.1.28'
serverPort = 5581
Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
Sock.connect((serverName,serverPort)) 
name = input('Input your Name')
city = input('Birthplace')
message = "Your name is :"+ name +", and you were born in:"+city
Sock.send(message.encode())
modifiedmessage = Sock.recv(1024) 
print ('From Server:', modifiedmessage.decode())
Sock.close()


# In[ ]:




