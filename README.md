<h1>Network Scanner</h1>


<h2>Description</h2>
- Network scanner script <br>
<br>This Python script performs a network scan to discover devices connected to a specified subnet. By sending ARP (Address Resolution Protocol) requests and analyzing the responses, it can identify the IP and MAC addresses of devices on the network. This script is useful for network administrators and security professionals to monitor and manage network devices.<br>

<br>Features: <br>
- Command-Line Interface:Easily specify the target IP address range for scanning.<br>
- ARP Requests: Sends ARP requests to the specified subnet and listens for responses.<br>
- Result Display: Prints the IP and MAC addresses of discovered devices in a well-formatted table.<br>
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 


<h2>Environments Used </h2>

- <b>Linux</b> 

<h2>Usage: </h2>
 Run the script with the required options:
<br>python network_scanner.py -t <target_ip_range>
<br>Example:
<br>python network_scanner.py -t 192.168.1.1/24
