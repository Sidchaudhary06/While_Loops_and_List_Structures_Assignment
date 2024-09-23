def find_min_max():
    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to quit): ")

        if user_input == "":
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if numbers:  # Check if the list is not empty
        print(f"Smallest number: {min(numbers)}")
        print(f"Largest number: {max(numbers)}")
    else:
        print("No numbers were entered.")

find_min_max()
