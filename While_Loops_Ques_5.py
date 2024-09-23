def login_system():
    correct_username = "python"
    correct_password = "rules"
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Welcome!")
            return
        else:
            attempts += 1
            print(f"Incorrect login. You have {max_attempts - attempts} attempt(s) left.")

    print("Access denied.")


login_system()
