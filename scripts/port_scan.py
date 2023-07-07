import nmap

target = "192.168.1.14/24"  # Replace with your target IP

nm = nmap.PortScanner()
nm.scan(hosts=target, arguments="-p 1-65535 -sV")
scan_results = nm[target]

open_ports = scan_results["tcp"].keys()

for port in open_ports:
    print("Port:", port)
    print("Service:", scan_results["tcp"][port]["name"])
