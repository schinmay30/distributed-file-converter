import socket
import os
import threading
import logging
from converter import convert_file

HOST = '127.0.0.1'
PORT = 5000

# 🔥 Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s - %(message)s'
)

os.makedirs("converted", exist_ok=True)
os.makedirs("test_files", exist_ok=True)

def handle_client(conn, addr):
    logging.info(f"Client connected: {addr}")

    try:
        filename = conn.recv(1024).decode()
        data = conn.recv(4096).decode()

        logging.info(f"Received file: {filename}")

        input_path = f"test_files/{filename}"
        output_path = f"converted/converted_{filename}"

        with open(input_path, "w") as f:
            f.write(data)

        success = convert_file(input_path, output_path)

        if success:
            logging.info(f"Conversion successful: {filename}")
            conn.send("File converted successfully".encode())
        else:
            logging.error(f"Conversion failed: {filename}")
            conn.send("Conversion failed".encode())

    except Exception as e:
        logging.error(f"Error handling client {addr}: {e}")

    conn.close()
    logging.info(f"Connection closed: {addr}")

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

logging.info("Server started...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()