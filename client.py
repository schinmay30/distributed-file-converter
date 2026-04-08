import socket

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

filename = "sample.txt"
content = "Hello this is a distributed system project"

client.send(filename.encode())
client.send(content.encode())

response = client.recv(1024).decode()
print("Server response:", response)

client.close()
