def load_users():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        pass
    return users



def save_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")



users = load_users()



def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        print("User already exists!")
    else:
        users[username] = password
        save_user(username, password)
        print("Registered successfully!")



def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if users.get(username) == password:
        print("Login successful!")
    else:
        print("Invalid credentials!")



while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")