import socket
import sys
import os

if len(sys.argv) != 3:
    print("Usage: python client.py <file_path> <conversion_type>")
    print("Example: python client.py test_files/sample.txt txt_to_docx")
    sys.exit(1)

HOST = "localhost"
PORT = 9000

file_path = sys.argv[1]
conversion_type = sys.argv[2]

if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)

with open(file_path, "rb") as f:
    file_data = f.read()

payload = conversion_type.encode() + b"||" + file_data

sock = socket.socket()
sock.connect((HOST, PORT))
sock.send(b'C')   # identify as client

# Send length prefix + payload
sock.send(len(payload).to_bytes(4, 'big'))
sock.sendall(payload)
print(f"[Client] Sent {len(payload)} bytes to master")

result = sock.recv(10000000)
sock.close()

if result.startswith(b"ERROR:"):
    print("Server error:", result.decode())
    sys.exit(1)

os.makedirs("converted", exist_ok=True)
if "_to_" in conversion_type:
    output_ext = conversion_type.split("_to_")[1]
else:
    output_ext = "bin"
output_file = f"converted/output.{output_ext}"

with open(output_file, "wb") as f:
    f.write(result)

print(f"\n[Client] Conversion completed! Output saved to: {output_file}")