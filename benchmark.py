import time
import subprocess

start = time.time()
subprocess.run(["python", "client.py"])
end = time.time()

print(f"Execution time: {end - start:.4f} seconds")
