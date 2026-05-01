def perform_operation(num1, num2, choice):
    """Perform the selected operation and return the result."""
    if choice == '1':
        return f"{num1} + {num2} = {num1 + num2}"
    elif choice == '2':
        return f"{num1} - {num2} = {num1 - num2}"
    elif choice == '3':
        return f"{num1} * {num2} = {num1 * num2}"
    elif choice == '4':
        if num2 != 0:
            return f"{num1} / {num2} = {num1 / num2}"
        else:
            return "Error: Cannot divide by zero!"
    elif choice == '5':
        if num2 != 0:
            return f"{num1} % {num2} = {num1 % num2}"
        else:
            return "Error: Cannot perform modulo by zero!"
    elif choice == '6':
        return f"{num1} ** {num2} = {num1 ** num2}"
    else:
        return "Invalid choice! Please select a valid operation."

def read_from_file(filename):
    """Read two integers and operation choice from file."""
    try:
        with open(filename, 'r') as f:
            num1 = int(f.readline().strip())
            num2 = int(f.readline().strip())
            choice = f.readline().strip()
        return num1, num2, choice
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None, None, None
    except ValueError:
        print("Error: File must contain two integers and an operation choice!")
        return None, None, None

def write_to_file(filename, result):
    """Write the result to a file."""
    with open(filename, 'a') as f:
        f.write(result + "\n")
    print(f"Result written to {filename}")

def calculator_interactive():
    """Interactive calculator mode."""
    print("=== Simple Calculator (Interactive Mode) ===")
    
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
    result = perform_operation(num1, num2, choice)
    print(f"\n{result}")
    
    # Ask if user wants to save to file
    save = input("\nSave result to file? (y/n): ").lower()
    if save == 'y':
        filename = input("Enter filename (default: results.txt): ").strip() or "results.txt"
        write_to_file(filename, result)

def calculator_file_mode():
    """File-based calculator mode."""
    print("=== Simple Calculator (File Mode) ===")
    input_file = input("Enter input filename (default: input.txt): ").strip() or "input.txt"
    output_file = input("Enter output filename (default: output.txt): ").strip() or "output.txt"
    
    num1, num2, choice = read_from_file(input_file)
    
    if num1 is not None:
        result = perform_operation(num1, num2, choice)
        print(f"\nResult: {result}")
        write_to_file(output_file, result)

if __name__ == "__main__":
    print("=== Calculator Menu ===")
    print("1. Interactive Mode")
    print("2. File Mode (Read from file, Write to file)")
    
    mode = input("\nSelect mode (1/2): ")
    
    if mode == '1':
        calculator_interactive()
    elif mode == '2':
        calculator_file_mode()
    else:
        print("Invalid choice!")