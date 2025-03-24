#!/usr/bin/env python3
import nmap
from datetime import datetime
import os

# Initialize the Nmap scanner
scanner = nmap.PortScanner()

# Set target (Juice Shop running on localhost)
target = "127.0.0.1"

# Scan target for vulnerabilities (HTTP, Node.js, etc.)
print(f"[*] Scanning {target} for vulnerabilities...")
scanner.scan(target, arguments='-sV --script vulners -p 3000,80,21,22')

# Debug: Print scan results
print("[*] Scan results:")
print(scanner[target])

# Generate a markdown report
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_file = f"vuln_report_{timestamp}.md"
print(f"[*] Report file: {report_file}")

# Write the report
try:
    with open(report_file, "w") as f:
        f.write(f"# Vulnerability Report ({timestamp})\n")
        f.write(f"**Target IP**: {target}\n\n")
        
        if 'tcp' in scanner[target]:
            f.write("## Open Ports & CVEs\n")
            for port in scanner[target]['tcp']:
                service = scanner[target]['tcp'][port]['name']
                product = scanner[target]['tcp'][port]['product']
                version = scanner[target]['tcp'][port]['version']
                cves = scanner[target]['tcp'][port].get('script', {}).get('vulners', 'No CVEs found')
                
                f.write(f"### Port {port} ({service})\n")
                f.write(f"- **Product**: {product} {version}\n")
                f.write(f"- **CVEs**:\n```\n{cves}\n```\n\n")
        
        # Add recommendations
        f.write("## Risk Mitigation Recommendations\n")
        f.write("- Update outdated software (e.g., Node.js)\n")
        f.write("- Disable unused services (e.g., FTP on port 21)\n")
        f.write("- Enable HTTPS for secure communication\n")

    print(f"[+] Report saved as {report_file}")
except Exception as e:
    print(f"[-] Error writing report: {e}")
