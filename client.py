import socket
target_host = socket.gethostbyname(socket.gethostname())
target_port = 1234

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
c.connect((target_host, target_port))
#print(f"connecting to {target_host: target_port}")

data = input ("Enter the message!\n")
c.send(data.encode('utf-8'))
response = c.recv(1024)

print(response.decode('utf-8'))

c.close
