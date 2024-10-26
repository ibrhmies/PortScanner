# **Port Scanner**

A simple Python-based port scanner that allows you to scan a custom range of ports or commonly used ports on a target host. The results are saved to a text file for review.

## **Features**
- Scan custom port ranges.
- Scan commonly used ports (e.g., 21, 22, 80, 443).
- Timeout setting for faster or slower scans.
- Save scan results to a detailed report file.
- Handles user interruption (Ctrl+C) gracefully.

## **Common Ports Scanned**
- Ports include: 20 (FTP), 21 (FTP), 22 (SSH), 25 (SMTP), 53 (DNS), 80 (HTTP), 110 (POP3), 143 (IMAP), 443 (HTTPS), 445 (SMB), 587 (SMTP over TLS), 993 (IMAP over SSL), 995 (POP3 over SSL), 3306 (MySQL), 3389 (RDP), 8080 (HTTP Alternative), and many more.

## **Usage**

### **Requirements**
- Python 3.x
- No additional libraries needed (uses Python's standard `socket` and `datetime` libraries).

### **Installation**
1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/ibrhmies/PortScanner.git
   cd PortScanner
   ```

2. Make sure you have Python 3 installed. You can check your Python version with:
   ```bash
   python --version
   ```

### **Running the Script**
To run the port scanner, use the following command:
```bash
python portscan.py
```

### **Options**
Upon running the script, you will be prompted with two options:

1. **Custom Port Range**: Enter a custom range of ports to scan.
   - Example input: 
     ```
     Enter Target Host: 192.168.1.1
     Enter Target Port Min: 20
     Enter Target Port Max: 100
     ```
   - The scanner will scan ports 20 to 100 on the target host.

2. **Common Ports**: Choose this option to scan a predefined list of frequently used ports.
   - Example input:
     ```
     Enter Target Host: 192.168.1.1
     ```

### **Output**
- The scan results will be displayed on the console.
- A detailed report will be saved to a file named `port_scan_report.txt` in the same directory.

## **Example Output**
```
Port Scan Report
Target Host: 192.168.1.1
Scan Date: 2024-10-26 12:45:23.678910
========================================
Port 22: OPEN
Port 80: CLOSED
Port 443: OPEN
...
```

## **Code Structure**

- **common_ports**: A list of frequently used ports.
- **portScanner**: Function that performs the port scan and logs results to the console and file.
- **User Input**: Option to choose between custom port range or common ports.

## **Notes**
- This script is for educational purposes only. Do not use it to scan unauthorized or unknown systems.
- Use a safe test environment or IPs such as `scanme.nmap.org` or test IP ranges like `192.0.2.0/24`.

## **License**
This project is licensed under the MIT License - see the LICENSE file for details.

## **Author**
- **İbrahim Eren SEVEN** - Initial work - [GitHub Profile](https://github.com/ibrhmies)
