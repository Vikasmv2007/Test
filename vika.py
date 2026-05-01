def calculator():
    print("=== Simple Calculator ===")
    
    # Input two integers
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
    
    # Display menu
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulo (%)")
    print("6. Power (**)")
    
    choice = input("\nEnter choice (1/2/3/4/5/6): ")
    
    # Perform operation
    if choice == '1':
        print(f"\n{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"\n{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"\n{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"\n{num1} / {num2} = {num1 / num2}")
        else:
            print("\nError: Cannot divide by zero!")
    elif choice == '5':
        if num2 != 0:
            print(f"\n{num1} % {num2} = {num1 % num2}")
        else:
            print("\nError: Cannot perform modulo by zero!")
    elif choice == '6':
        print(f"\n{num1} ** {num2} = {num1 ** num2}")
    else:
        print("\nInvalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()