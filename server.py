import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 65432

# User credentials
users = {
    "apple": "apple123",
    "banana": "banana123",
    "cherry": "cherry123",
    "alice": "alice123",
    # Add other users as needed
}

# Placeholder for friends list
friends = {
    "apple": ["Banana", "Cherry"],
    "banana": ["alice"],
    "cherry": ["apple"]
    # Add default friends for other users as needed
}

def handle_client(conn, addr):
    print(f"Connected by {addr}")

    try:
        conn.sendall("Welcome to Message System\nPlease login\nYour user ID: ".encode())
        user_id = conn.recv(1024).decode().strip()

        conn.sendall("Your password: ".encode())
        password = conn.recv(1024).decode().strip()

        if user_id in users and users[user_id] == password:
            conn.sendall("Login successful!\n".encode())
        else:
            conn.sendall("Login failed. Please try again.\n".encode())
            return

        while True:
            # Main menu
            conn.sendall("Welcome to Message System\n----------------------\nPlease choose one of the following options:\n1. Manage your friend list\n2. Send message to your friend(s)\n3. Send file to your friend(s)\n4. View your messages and files\n5. Logout\nYour Option: ".encode())
            menu_choice = conn.recv(1024).decode().strip()

            if menu_choice == "1":
                # Send submenu
                conn.sendall("Manage your friend list\n-----------------------\n1. View friends\n2. Add friend\n3. Remove friend\nYour Option: ".encode())
                submenu_choice = conn.recv(1024).decode().strip()  # Ensure this recv is here to wait for the client's choice
                # Process submenu choice
                if submenu_choice == "1":
                    friend_list = ", ".join(friends.get(user_id, []))
                    conn.sendall(f"Your friends: {friend_list}\n".encode())
                # Add handling for other submenu choices (e.g., Add friend, Remove friend)
            elif menu_choice == "5":
                # Process logout
                conn.sendall("Logging out...\n".encode())
                break  # Exit the loop to end the client session
    finally:
        print(f"Disconnected from {addr}")
        conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server is starting...")

        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    main()