def you_add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
  
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def main() :
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Choose an operation (1/2/3/4/5): ")

    if choice == '1':
       num1 = float(input("Enter first number: "))
       num2 = float(input("Enter second number: "))
       print(f"The result is: {your_add(num1, num2)}")
    elif choice == '2':
       num1 = float(input("Enter first number: "))
       num2 = float(input("Enter second number: "))
       print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4':
       num1 = float(input("Enter first number: "))
       num2 = float(input("Enter second number: "))
       print(f"The result is: {divide(num1, num2)}")
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
    else:
        print("Invalid choice. Please select a valid operation.")
    
if __name__ == "__main__":
    main()
