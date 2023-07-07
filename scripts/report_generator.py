import threading

def generate_report(scan_results):
    report = ""

    for host in scan_results:
        report += f"Host: {host}\n"
        open_ports = scan_results[host]["tcp"].keys()

        for port in open_ports:
            report += f"Port: {port}\n"
            report += f"Service: {scan_results[host]['tcp'][port]['name']}\n"

        report += "\n"

    # Save or print the report as needed
    print(report)


# Sample scan results (replace with your actual scan results)
sample_scan_results = {
    "192.168.1.14": {
        "tcp": {
            "22": {
                "name": "ssh"
            },
            "80": {
                "name": "http"
            }
        }
    },
    "192.168.1.15": {
        "tcp": {
            "443": {
                "name": "https"
            }
        }
    }
}

# Create a thread for generating the report
thread = threading.Thread(target=generate_report, args=(sample_scan_results,))
thread.start()
thread.join()
