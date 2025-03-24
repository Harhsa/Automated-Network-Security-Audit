from zapv2 import ZAPv2
import time

# Connect to ZAP
zap = ZAPv2(apikey='12345', proxies={'http': 'http://localhost:8080', 'https': 'http://localhost:8080'})

# Target URL (Juice Shop)
target = 'http://localhost:3000'

# Start scan
print('Starting scan...')
zap.urlopen(target)  # Open the target URL
scan_id = zap.ascan.scan(target)  # Start active scan

# Wait for scan to complete
while int(zap.ascan.status(scan_id)) < 100:
    print(f'Scan progress: {zap.ascan.status(scan_id)}%')
    time.sleep(10)

# Generate report
report_html = zap.core.htmlreport()
with open('zap_report.html', 'w') as f:
    f.write(report_html)

print('Report saved as zap_report.html!')
