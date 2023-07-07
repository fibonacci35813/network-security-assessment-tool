import nmap
import threading

target = "192.168.1.14"  # Replace with your target IP
open_ports = []

# Function to scan a specific port
def scan_port(port):
    nm = nmap.PortScanner()
    result = nm.scan(hosts=target, ports=str(port), arguments="-sV")

    if result["scan"][target]["tcp"][port]["state"] == "open":
        open_ports.append(port)

# Create a list of ports to scan
ports_to_scan = range(1, 65536)

# Create a thread for each port
threads = []
for port in ports_to_scan:
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print open ports
for port in open_ports:
    print("Port:", port)
