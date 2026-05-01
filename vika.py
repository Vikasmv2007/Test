import math

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

def perform_scientific_operation(num, choice):
    """Perform scientific operations on a single number."""
    try:
        if choice == '1':
            return f"√{num} = {math.sqrt(num)}"
        elif choice == '2':
            return f"sin({num}°) = {math.sin(math.radians(num))}"
        elif choice == '3':
            return f"cos({num}°) = {math.cos(math.radians(num))}"
        elif choice == '4':
            return f"tan({num}°) = {math.tan(math.radians(num))}"
        elif choice == '5':
            return f"log₁₀({num}) = {math.log10(num)}"
        elif choice == '6':
            return f"ln({num}) = {math.log(num)}"
        elif choice == '7':
            return f"e^{num} = {math.exp(num)}"
        elif choice == '8':
            return f"{num}! = {math.factorial(int(num))}"
        elif choice == '9':
            return f"|{num}| = {abs(num)}"
        elif choice == '10':
            return f"sin⁻¹({num}) = {math.degrees(math.asin(num))}°"
        elif choice == '11':
            return f"cos⁻¹({num}) = {math.degrees(math.acos(num))}°"
        elif choice == '12':
            return f"tan⁻¹({num}) = {math.degrees(math.atan(num))}°"
        else:
            return "Invalid choice!"
    except ValueError as e:
        return f"Error: {e}"

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

def scientific_calculator():
    """Scientific calculator mode."""
    print("\n=== Scientific Calculator ===")
    print("Performing single-number scientific operations\n")
    
    num = float(input("Enter a number: "))
    
    print("\nSelect operation:")
    print("1. Square Root (√)")
    print("2. Sine (sin)")
    print("3. Cosine (cos)")
    print("4. Tangent (tan)")
    print("5. Log₁₀ (log base 10)")
    print("6. Natural Log (ln)")
    print("7. Exponential (e^x)")
    print("8. Factorial (!)")
    print("9. Absolute Value (|x|)")
    print("10. Inverse Sine (sin⁻¹)")
    print("11. Inverse Cosine (cos⁻¹)")
    print("12. Inverse Tangent (tan⁻¹)")
    
    choice = input("\nEnter choice (1-12): ")
    result = perform_scientific_operation(num, choice)
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
    print("1. Interactive Mode (Basic)")
    print("2. Scientific Mode")
    print("3. File Mode (Read from file, Write to file)")
    
    mode = input("\nSelect mode (1/2/3): ")
    
    if mode == '1':
        calculator_interactive()
    elif mode == '2':
        scientific_calculator()
    elif mode == '3':
        calculator_file_mode()
    else:
        print("Invalid choice!")

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