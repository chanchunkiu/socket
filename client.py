import socket
# Server configuration
HOST = '127.0.0.1'
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Connected to the server.")

        # Receive and print the welcome message along with the user ID prompt from the server
        welcome_and_user_id_prompt = s.recv(1024).decode()
        print(welcome_and_user_id_prompt, end='')  # Use end='' to avoid adding an extra newline

        # Send user ID
        user_id = input()  # No prompt needed, as the server provides it
        s.sendall(user_id.encode())

        # Receive and print the password prompt from the server
        password_prompt = s.recv(1024).decode()
        print(password_prompt, end='')  # Use end='' to avoid adding an extra newline

        # Send password
        password = input()  # No prompt needed, as the server provides it
        s.sendall(password.encode())

        # Receive authentication result
        auth_result = s.recv(1024).decode()
        print(auth_result)

        # Handle server responses after authentication
        if "successful" in auth_result:
            while True:
                command = input("Enter command: ")
                s.sendall(command.encode())

                # Receive server commands or messages after sending command
                server_response = s.recv(1024).decode()
                print(server_response)

                if command == "5":  # Assuming "exit" is the command to break the loop
                    break

        print("Disconnected from the server.")

if __name__ == "__main__":
    main()