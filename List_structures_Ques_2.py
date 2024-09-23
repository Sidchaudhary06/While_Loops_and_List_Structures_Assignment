def find_top_five():
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

    if numbers:
        numbers.sort(reverse=True)
        top_five = numbers[:5]
        print(f"The five greatest numbers are: {top_five}")
    else:
        print("No numbers were entered.")


find_top_five()
