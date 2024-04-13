import socket
import threading

#server
HOST = '127.0.0.1'
PORT = 65432

# User
users = {
    "apple": "apple123",
    "banana": "banana123",
    "cherry": "cherry123",
    "alice": "alice123",
    # Add other users as needed
}

#friends
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
            # Main
            conn.sendall("Welcome to Message System\n----------------------\nPlease choose one of the following options:\n1. Manage your friend list\n2. Send message to your friend(s)\n3. Send file to your friend(s)\n4. View your messages and files\n5. Logout\nYour Option: ".encode())
            menu_choice = conn.recv(1024).decode().strip()

            if menu_choice == "1":
                #Friend
                conn.sendall("Manage your friend list\n-----------------------\n1. View friends\n2. Add friend\n3. Remove friend\nYour Option: ".encode())
                submenu_choice = conn.recv(1024).decode().strip()  # Ensure this recv is here to wait for the client's choice
                # Process submenu choice
                if submenu_choice == "1":
                    friend_list = friends.get(user_id, [])
                    friend_list_formatted = "\n".join(friend_list)
                    conn.sendall(f"View your friends\n------------------------------------\n{friend_list_formatted}".encode())
                    # Wait for the client to signal that the user pressed Enter
                    conn.recv(1024)
            elif menu_choice == "5":
                #logout
                conn.sendall("Logging out...\n".encode())
                break  #exit
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