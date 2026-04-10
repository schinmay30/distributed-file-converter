import socket
import threading

HOST = "localhost"
PORT = 9000

workers = []
worker_lock = threading.Lock()
worker_index = 0

def handle_worker(conn):
    with worker_lock:
        workers.append(conn)
    print(f"[Master] Worker connected. Total workers: {len(workers)}")
    # Keep connection alive – just wait for disconnect
    while True:
        if conn.recv(1, socket.MSG_PEEK) == b'':
            break
    with worker_lock:
        if conn in workers:
            workers.remove(conn)
    conn.close()
    print("[Master] Worker disconnected")

def handle_client(conn):
    global worker_index
    # Read the 4-byte length of the incoming job
    raw_len = conn.recv(4)
    if not raw_len:
        conn.close()
        return
    data_len = int.from_bytes(raw_len, 'big')
    print(f"[Master] Expecting {data_len} bytes from client")

    payload = b''
    while len(payload) < data_len:
        chunk = conn.recv(min(4096, data_len - len(payload)))
        if not chunk:
            break
        payload += chunk
    print(f"[Master] Received {len(payload)} bytes from client")

    with worker_lock:
        if not workers:
            conn.send(b"ERROR: No worker available")
            conn.close()
            return
        worker = workers[worker_index]
        worker_index = (worker_index + 1) % len(workers)

    # Forward the job to the worker (with length prefix)
    worker.send(raw_len)   # send the original 4-byte length
    worker.sendall(payload)
    print("[Master] Job forwarded to worker")

    # Wait for worker's result (also length-prefixed)
    res_len_raw = worker.recv(4)
    if not res_len_raw:
        conn.send(b"ERROR: Worker failed")
        conn.close()
        return
    res_len = int.from_bytes(res_len_raw, 'big')
    result = b''
    while len(result) < res_len:
        chunk = worker.recv(min(4096, res_len - len(result)))
        if not chunk:
            break
        result += chunk
    print(f"[Master] Received {len(result)} bytes from worker")

    conn.sendall(result)
    conn.close()
    print("[Master] Result sent to client")

def start_server():
    server = socket.socket()
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[Master] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        # Read exactly 1 byte to determine role
        role_byte = conn.recv(1)
        if not role_byte:
            conn.close()
            continue
        if role_byte == b'W':
            threading.Thread(target=handle_worker, args=(conn,), daemon=True).start()
        elif role_byte == b'C':
            threading.Thread(target=handle_client, args=(conn,), daemon=True).start()
        else:
            conn.close()

if __name__ == "__main__":
    start_server()