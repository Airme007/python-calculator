# Function to perform calculations
def calculate():
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        user_choice = input("Input your choice (1/2/3/4/5): ")

        if user_choice == '5':
            print("Exiting Calculator. Goodbye!")
            break

        if user_choice in ('1', '2', '3', '4'):
            num_one = float(input("Enter first number: "))
            num_two = float(input("Enter second number: "))

            if user_choice == '1':
                print("Result:", num_one + num_two)
            elif user_choice == '2':
                print("Result:", num_one - num_two)
            elif user_choice == '3':
                print("Result:", num_one * num_two)
            elif user_choice == '4':
                print("Result:", num_one / num_two if num_two != 0 else "Error: Division by zero")
        else:
            print("Invalid choice! Please select a valid operation.")

# Run the calculator
calculate()

