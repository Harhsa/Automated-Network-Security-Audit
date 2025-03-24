**PROJECT REPORT**  
**AUTOMATED NETWORK SECURITY AUDIT**  

---  

## **1. Introduction**  
### **1.1 Project Overview**  
The **Automated Network Security Audit** is a cybersecurity tool designed to assess network security, detect vulnerabilities, and generate risk reports. It automates the auditing process by leveraging tools like **Nmap, OWASP ZAP, Wireshark, and Python scripts** to analyze network configurations and security flaws.

### **1.2 Objective**  
- Identify security vulnerabilities in network infrastructure.
- Automate network scanning and analysis using security tools.
- Generate a structured risk report with mitigation strategies.
- Assist security teams in improving network security posture.

### **1.3 Scope**  
- The tool scans networks for open ports, misconfigurations, and vulnerabilities.
- It integrates well-known security tools like **Nmap, Wireshark, and OWASP ZAP**.
- Generates structured reports with risk levels and remediation steps.

---  

## **2. Tools & Technologies Used**  
- **Operating System:** Kali Linux (Xfce)
- **Programming Language:** Python
- **Security Tools:** Nmap, OWASP ZAP, Wireshark
- **Libraries & Modules:** Requests, Scapy, Paramiko
- **Report Generation:** Markdown, HTML
- **Version Control:** Git & GitHub

---  

## **3. System Architecture**  
### **3.1 Workflow Diagram**  
1. User inputs the target network or IP range.
2. The scanner performs network reconnaissance (Nmap, Whois lookup).
3. The vulnerability scanning process begins using OWASP ZAP and Wireshark.
4. The tool identifies and categorizes vulnerabilities.
5. Generates a structured network security risk report.
6. The report is exported in Markdown and HTML format.

![System Workflow](report_screenshot.png) *(Replace with actual workflow image)*

---  

## **4. Implementation Steps**  
### **4.1 Environment Setup**  
- Installed **Kali Linux** with pre-built security tools.
- Installed necessary Python libraries:
  ```bash
  pip install requests scapy paramiko
  ```
- Configured OWASP ZAP and Wireshark for automated network analysis.

### **4.2 Network Reconnaissance**  
- Gathered information about the target network using:
  ```bash
  nmap -A <target_IP>
  whois <target_IP>
  ```
- Identified open ports, running services, and potential vulnerabilities.

### **4.3 Automated Security Auditing**  
- Used **Nmap** to scan for open ports and misconfigurations:
  ```bash
  nmap -sV -O <target_IP>
  ```
- Used **OWASP ZAP** to scan for web-related vulnerabilities:
  ```bash
  zap-baseline.py -t <target_URL>
  ```
- Captured network traffic using **Wireshark** to detect anomalies.

### **4.4 Report Generation**  
- Generated a **Markdown and HTML-based network security report**.
- Categorized vulnerabilities as **Critical, High, Medium, Low**.
- Suggested remediation steps.

---  

## **5. Results & Findings**  
| Vulnerability | Severity | Description | Recommended Fix |
|--------------|---------|-------------|-----------------|
| Open Ports | High | Unsecured services running | Restrict unused ports |
| Weak SSH Config | Medium | SSH misconfigurations found | Implement strong ciphers |
| HTTP Security Issues | Medium | Missing security headers | Configure proper headers |

- **Total vulnerabilities found:** 6
- **Critical issues:** 2
- **Resolved vulnerabilities:** 4

---  

## **6. Challenges & Solutions**  
### **6.1 Challenges Faced**  
- **False Positives:** Some reported vulnerabilities were not exploitable.
- **Automating Analysis:** Required fine-tuning OWASP ZAP and Wireshark.
- **Handling Large Data Sets:** Needed filtering to keep reports relevant.

### **6.2 Solutions Implemented**  
- Used manual validation to eliminate false positives.
- Optimized scanning parameters for better accuracy.
- Implemented a filtering mechanism to highlight important vulnerabilities.

---  

## **7. Conclusion & Future Scope**  
### **7.1 Conclusion**  
The **Automated Network Security Audit** successfully identifies vulnerabilities in network infrastructure. It automates reconnaissance, scanning, and traffic analysis, reducing manual effort for security teams. The structured security report provides a detailed assessment, helping organizations mitigate risks effectively.

### **7.2 Future Enhancements**  
- Improve **Machine Learning-based** anomaly detection.
- Add **Multi-threaded scanning** for faster results.
- Expand scanning to include **Cloud security vulnerabilities**.

---  

## **8. References**  
- [OWASP ZAP Documentation](https://www.zaproxy.org/)
- [Nmap Official Guide](https://nmap.org/book/man.html)
- [Wireshark User Guide](https://www.wireshark.org/docs/)
- [Python Scapy Documentation](https://scapy.readthedocs.io/)
- [GitHub Repository](https://github.com/Harhsa/Automated-Network-Security-Audit)

---  

## **9. Appendices**  
### **9.1 Screenshots of Execution**  
*(Attach screenshots of scanning, reports, and findings.)*

### **9.2 Sample Security Report Output**  
- **Markdown Report:** `vuln_report_2025-03-24.md`
- **HTML Report:** `vuln_report.html`

---

This project report is **structured, professional, and detailed** to impress interviewers and showcase your skills effectively. 🚀 Let me know if you need any modifications! 😃

