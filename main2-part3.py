import socket

def http_get_request(host, port, user_id):
    try:
        with socket.create_connection((host, port), timeout=1) as sock:
            request = f"GET {user_id}\n"
            sock.sendall(request.encode())
            response = sock.recv(1024).decode()
            return response
    except (socket.error, socket.timeout):
        return "Error: Unable to send GET request"

def http_post_request(host, port, user_name, user_age):
    try:
        with socket.create_connection((host, port), timeout=1) as sock:
            request = f"POST {user_name} {user_age}\n"
            sock.sendall(request.encode())
            response = sock.recv(1024).decode()
            return response
    except (socket.error, socket.timeout):
        return "Error: Unable to send POST request"

if __name__ == "__main__":
    target_host = 'localhost'
    target_port = 8080

    while True:
        print("\nChoose an option:")
        print("1. Perform GET request")
        print("2. Perform POST request")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            user_id = input("Enter the user ID for GET request (e.g., user1): ")
            response = http_get_request(target_host, target_port, user_id)
            print(f"GET Response: {response}")
        elif choice == "2":
            user_name, user_age = input("Enter user information (name age): ").split()
            response = http_post_request(target_host, target_port, user_name, user_age)
            print(f"POST Response: {response}")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
