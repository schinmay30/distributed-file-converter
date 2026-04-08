import socket

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

filename = "sample.txt"

with open(filename, "r") as f:
    data = f.read()

# 🔥 IMPORTANT: send filename + data
client.sendall(filename.encode())
client.sendall(data.encode())

response = client.recv(1024).decode()
print("Server:", response)

client.close()