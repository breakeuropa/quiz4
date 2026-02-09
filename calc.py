def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main() :
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Choose an operation (1/2/3/4/5): ")

    if choice == '1':
       print(f"Adding 1 + 2 = {add(1,2)}")
    elif choice == '2':
        print(f"Subtracting 7 - 3 = {subtract(7,3)}")
    elif choice == '3':
        print("Invalid choice. Please select a valid operation.")
    elif choice == '4':
        print("Invalid choice. Please select a valid operation.")
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
    else:
        print("Invalid choice. Please select a valid operation.")
    
if __name__ == "__main__":
    main()