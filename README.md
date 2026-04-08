# 📁 Distributed File Converter System

## Overview

A Python-based distributed system that allows multiple clients to send files to a server for processing and conversion. The system supports concurrent client connections, structured logging, and real-time file conversion.

---

## Features

* Multi-client support using threading
* Client-server architecture using sockets
* Real-time file transfer and processing
* Structured logging system for monitoring
* File conversion (TXT → PDF)
* Scalable and modular design

---

##  Tech Stack

* Python
* Socket Programming
* Threading
* Logging
* FPDF (for PDF conversion)

---

##  How It Works

1. Client sends a file to the server
2. Server receives and stores the file
3. File is processed and converted
4. Converted file is saved in output folder
5. Server sends response back to client

---

## ▶️ How to Run

### Step 1: Install dependencies

```bash
pip install fpdf
```

### Step 2: Start Server

```bash
python master_server.py
```

### Step 3: Run Client

```bash
python client.py
```

---

## 📂 Project Structure

```
distributed_file_converter/
│── client.py
│── master_server.py
│── converter.py
│── test_files/
│── converted/
│── README.md
```

---

## Example

Input:

```
sample.txt
```

Output:

```
converted_sample.pdf
```

---

## Future Improvements

* Support for multiple file formats (images, docs)
* Web-based interface
* Cloud deployment
* File compression and encryption

---


