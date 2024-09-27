# ThreadedPortScan
PortPulse
A Multi-threaded Port Scanner for Efficient Network Security Testing

Overview
PortPulse is a high-performance, multi-threaded port scanning tool designed to identify open ports on a target system or network. Built for speed and scalability, PortPulse leverages multi-threading to significantly reduce scan times, making it ideal for both small networks and large-scale security assessments.

The tool prompts the user for an IP address and a port range, then rapidly scans the specified range to find open ports. The results are saved in a neatly formatted text file for easy analysis.

Features
Multi-threaded Scanning: Harnesses the power of multi-threading to efficiently scan thousands of ports in parallel, drastically reducing scan times.
Customizable Port Range: Specify the range of ports you want to scan, whether it’s a narrow set or a full range of 0-65535.
Open Port Detection: Accurately identifies and lists all open ports for the given IP address.
Result Export: Automatically saves scan results in a text file for further analysis or record-keeping.
User-friendly Input: Simple command-line interface that asks for the IP address and port range from the user.
Efficient Resource Usage: Optimized for minimal resource consumption while providing fast results.

How It Works
Input: The user is prompted to enter the target IP address and specify the port range to scan.
Multi-threaded Scan: The tool initiates a multi-threaded scan across the specified port range, checking for open ports.
Result Storage: Open ports are logged in real-time and saved to a text file upon completion.
