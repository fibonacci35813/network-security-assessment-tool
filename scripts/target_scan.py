import nmap
import threading

target_range = "192.168.1.14/24"  # Replace with your target IP range
scan_results = []

# Function to scan a specific target
def scan_target(target):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments="-sn")
    scan_results.append(nm.all_hosts())

# Create a list of targets to scan
targets_to_scan = [f"192.168.1.{i}" for i in range(1, 256)]

# Create a thread for each target
threads = []
for target in targets_to_scan:
    thread = threading.Thread(target=scan_target, args=(target,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print scan results
for result in scan_results:
    for host in result:
        print("Host:", host)
