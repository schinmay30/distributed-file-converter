import time
import subprocess
import os

# Ensure a test file exists
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("This is a benchmark test file.")

start = time.time()
subprocess.run(["python", "client.py", "sample.txt", "txt_to_pdf"])
end = time.time()

print(f"Execution time: {end - start:.4f} seconds")