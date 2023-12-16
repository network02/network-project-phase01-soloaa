import socket
from socket import getservbyport

def is_host_online(host, port):
    try:
        # Create a socket object
        sock = socket.create_connection((host, port), timeout=1)
        # Close the socket
        sock.close()
        return True
    except (socket.error, socket.timeout):
        return False

def scan_ports(host, port_range):
    start_port, end_port = map(int, port_range.split())
    open_ports = []

    for port in range(start_port, end_port + 1):
        if is_port_open(host, port):
            service_name = get_service_name(port)
            open_ports.append((port, service_name))

    return open_ports

def is_port_open(host, port):
    try:
        with socket.create_connection((host, port), timeout=1) as sock:
            return True
    except (socket.error, socket.timeout):
        return False

def get_service_name(port):
    try:
        service_name = getservbyport(port)
        return service_name
    except (socket.error, socket.herror):
        return "Unknown"


if __name__ == "__main__":
    target_host = input("Enter the target host: ")
    input_port = input("Enter a port number (e.g., 80) / port range(e.g., 80 85) to check : ")

    if any(char.isspace() for char in input_port): #part 2: scanning port
        port_range = input_port
        open_ports = scan_ports(target_host, port_range)

        if open_ports:
            print(f"{target_host} {port_range} has the following open ports:")
            for port, service_name in open_ports:
                print(f"{target_host} {port}: {service_name}")
        else:
            print(f"No open ports found on {target_host}.")

    else: #part1: if host is online

        target_port = int(input_port)
        if is_host_online(target_host, target_port):
            print(f"{target_host}:{target_port} is online.")
        else:
            print(f"{target_host}:{target_port} is offline.")

