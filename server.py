import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #define the ip version and the transport protocol to use

#bind he socket to a specific address and port 
server = (socket.gethostbyname(socket.gethostname()), 1234)
s.bind(server)

s.listen(5) #listen for incoming connections, the parameter is the max number of queued connections
print(f"Listening for incoming connections on {server}")

c, client = s.accept() #accept an incoming connection
print(f"Connection established with {client}")

# recieve data from the client
data = c.recv(1024)
print(data.decode('utf-8'))

# send a response back to the client 
response = "Hello from the server!"
c.send(response.encode('utf-8'))

# close the connection 
c.close()
s.close()
