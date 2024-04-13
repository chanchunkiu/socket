import socket
# Server configuration
HOST = '127.0.0.1'
PORT = 65432
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Connected to the server.")

        # Login process
        welcome_message = s.recv(1024).decode()
        print(welcome_message, end='')
        user_id = input().strip()  # Strip input here
        s.sendall(user_id.encode())

        password_prompt = s.recv(1024).decode()
        print(password_prompt, end='')
        password = input().strip()  # Strip input here
        s.sendall(password.encode())

        login_result = s.recv(1024).decode()
        print(login_result)

        while True:
            # Main menu
            main_menu = s.recv(1024).decode()
            print(main_menu, end='')
            main_menu_choice = input().strip()  # Strip input here
            s.sendall(main_menu_choice.encode())

            if main_menu_choice == "1":
                # Friend list management submenu
                submenu = s.recv(1024).decode()
                print(submenu, end='')
                submenu_choice = input().strip()  # Strip input here
                s.sendall(submenu_choice.encode())

                # Response to submenu choice
                submenu_response = s.recv(1024).decode()
                print(submenu_response)
            elif main_menu_choice == "5":
                # Handle logout
                logout_message = s.recv(1024).decode()
                print(logout_message)
                break  # Exit the loop to end the client session

        print("Disconnected from the server.")
        
if __name__ == "__main__":
    main()