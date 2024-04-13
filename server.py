import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 65432

# User credentials
users = {
    "apple": "apple123",
    "banana": "banana123",
    "lemon": "lemon123",
    "user4": "password4",
    "user5": "password5",
    "user6": "password6",
    "user7": "password7",
    "user8": "password8",
    "user9": "password9",
    "user10": "password10",
}

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        print("Server is starting...")
        while True:
            conn, addr = s.accept()
            print(f"Connected by {addr}")

            # Send welcome message and user ID prompt
            conn.sendall("Welcome to Message System\nPlease login\nYour user ID: ".encode())

            # Receive user ID from the client
            user_id = conn.recv(1024).decode().strip()
            print(f"Received user ID: {user_id}")

            # Send password prompt if user ID is received
            if user_id:
                conn.sendall("Your password: ".encode())

                # Receive password from the client
                password = conn.recv(1024).decode().strip()
                print(f"Received password: {password}")

                # Authentication logic
                if user_id in users and users[user_id] == password:
                    # Send authentication result to the client
                    conn.sendall("Login successful!".encode())
                else:
                    conn.sendall("Login failed. Please try again.".encode())

            print(f"Disconnected from {addr}")
            conn.close()

if __name__ == "__main__":
    main()
