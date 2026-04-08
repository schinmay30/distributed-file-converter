import socket
import os
from converter import convert_file

HOST = '127.0.0.1'
PORT = 5000

os.makedirs("converted", exist_ok=True)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("Server started... Waiting for client...")

while True:
    conn, addr = server.accept()
    print(f"Connected to {addr}")

    filename = conn.recv(1024).decode()
    data = conn.recv(4096).decode()

    input_path = f"test_files/{filename}"
    output_path = f"converted/converted_{filename}"

    os.makedirs("test_files", exist_ok=True)

    with open(input_path, "w") as f:
        f.write(data)

    success = convert_file(input_path, output_path)

    if success:
        conn.send("File converted successfully".encode())
    else:
        conn.send("Conversion failed".encode())

    conn.close()
