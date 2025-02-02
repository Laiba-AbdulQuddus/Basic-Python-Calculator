def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error Occured... Change the denominator please"
    else:   
        return a/b
def power(a, b):
    return a**b
def remainder(a, b):
    return a % b


print("Welcome to calculator. You can use operations like '+, -, /, *, **, %'. Type 'quit' to exit the program" )
while True:
    try:
        user_input = input("Enter calculation (e.g: 5 + 3) you want to perform. Type 'quit' to exit: ").strip()
        if user_input.lower() == 'quit':
            print("Thankyou for using the calculator. See you later. Good Bye!!")
            break

        
        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid Input. Use the format (e.g: 5 + 3)")
            continue
        a = float(parts[0])
        operation = parts[1].strip()
        b = float(parts[2])
        if operation == "+":
            print(f"Result: {add(a, b)}")
        elif operation == "-":
            print(f"Result: {subtract(a, b)}")
        elif operation == "*":
            print(f"Result: {multiply(a,b)}")
        elif operation == "/":
            print(f"Result: {divide(a,b)}")
        elif operation == "**":
            print(f"Result: {power(a,b)}")
        elif operation == "%":
            print(f"Result: {remainder(a,b)}")
        else:
            print("Invalid Operation. Enter the correct operation. ")
    except ValueError:
        print("The input entered is not a valid number. Enter the valid number please...")