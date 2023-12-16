import socket

def is_host_online(host, port):
    try:
        # Create a socket object
        sock = socket.create_connection((host, port), timeout=1)
        # Close the socket
        sock.close()
        return True
    except (socket.error, socket.timeout):
        return False

if __name__ == "__main__":
    target_host = input("Enter the target host: ")
    target_port = int(input("Enter a port number to check (e.g., 80 for HTTP): "))

    if is_host_online(target_host, target_port):
        print(f"{target_host}:{target_port} is online.")
    else:
        print(f"{target_host}:{target_port} is offline.")
