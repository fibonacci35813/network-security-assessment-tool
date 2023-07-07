import nmap

target = "192.168.1.14/24"  # Replace with your target IP range

nm = nmap.PortScanner()
nm.scan(hosts=target, arguments="-sn")
scan_results = nm.all_hosts()

for host in scan_results:
    print("Host:", host)
