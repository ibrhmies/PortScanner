import socket
from datetime import datetime

# A list of common ports that are frequently used in network communication
common_ports = [20, 21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 587, 993, 995,
                3306, 3389, 8080, 123, 161, 162, 389, 636, 1433, 1434, 5432, 6660, 6661, 6662,
                6663, 6664, 6665, 6666, 6667, 6668, 6669, 6697, 27017, 9200]

# Prompt user to choose between scanning a custom port range or common ports
print("Choose scan option:")
print("1. Custom port range")
print("2. Common ports (e.g., 21, 22, 80, 443, etc.)")
scan_option = input("Enter option (1 or 2): ")

# If the user enters an invalid option, keep asking for a valid option
if scan_option != '2' and scan_option != '1':
    print("Invalid option!")

    while scan_option != '2' and scan_option != '1':
        scan_option = input("Enter option (1 or 2): ")

# If option 1 is selected, ask for a custom target host and port range
if scan_option == "1":
    targetHost = input("Enter Target Host: ")
    targetPortmin = int(input("Enter Target Port Min: "))
    targetPortmax = int(input("Enter Target Port Max: "))
    port_list = list(range(targetPortmin, targetPortmax + 1)) # Create a list of ports to scan


# If option 2 is selected, scan common ports for the target host
elif scan_option == '2':
    targetHost = input("Enter Target Host: ")
    port_list = common_ports

else:
    print("Invalid option! Exiting...")
    exit()  # Exit the program if an invalid option is entered
    
# Define the output file name and location
output_file = "port_scan_report.txt"

# Open the file in write mode
with open(output_file, 'w') as file:
    # Add header and date information to the file
    file.write(f"Port Scan Report\n")
    file.write(f"Target Host: {targetHost}\n")
    file.write(f"Scan Date: {datetime.now()}\n")
    file.write("=" * 40 + "\n")

# Function to scan ports for the given target host
def portScanner(targetHost, port_list):
    with open(output_file, 'a') as file:   # Open the file in append mode
        for port in port_list:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1) # Set timeout duration to 1 second
                result = sock.connect_ex((targetHost, port))
                if result == 0:
                    print(f'Port {port} is open')
                    file.write(f'Port {port}: OPEN\n')  

                else:
                    print(f'Port {port} is closed')
                    file.write(f'Port {port}: CLOSED\n')  
                sock.close()

            except KeyboardInterrupt:
                print("Scan operation canceled") # Handle the user interrupt (Ctrl+C)
                break


            except socket.error as e:
                print(f"Socket error: {e}")  # Handle socket errors
                break

portScanner(targetHost, port_list)

print(f"Scan complete. Report saved to {output_file}")