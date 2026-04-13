import socket
import time

HOST = "localhost"
PORT = 9000

def send_request():
    try:
        sock = socket.socket()
        sock.connect((HOST, PORT))

        # SAME FORMAT AS CLIENT
        payload = b"lowercase||HELLO PERFORMANCE TEST"

        sock.send(b'C')  # identify as client
        sock.send(len(payload).to_bytes(4, 'big'))  # send length
        sock.sendall(payload)  # send actual data

        start = time.time()

        result = sock.recv(10000000)

        end = time.time()

        sock.close()

        return end - start

    except Exception as e:
        print("Request failed:", e)
        return None


times = []

for i in range(10):
    t = send_request()
    if t is not None:
        times.append(t)

# 🔥 FIX division error
if len(times) == 0:
    print("All requests failed ❌")
    exit()

avg_time = sum(times) / len(times)
throughput = len(times) / sum(times)

print("\n--- PERFORMANCE RESULTS ---")
print("Average Response Time:", round(avg_time, 5), "seconds")
print("Throughput:", round(throughput, 2), "jobs/sec")