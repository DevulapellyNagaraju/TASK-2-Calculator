# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to format and display the result
def display_result(num1, num2, operation, result):
    GREEN = "\033[32m"  # Green color code
    YELLOW = '\033[93m'
    ENDC = "\033[0m"  # Reset color code
    print(YELLOW + f"\n  {num1}" + ENDC)
    print(YELLOW + f"{operation} {num2}" + ENDC)
    print(f"{operation*16}")
    print(GREEN + f" Answer: {result}\n" + ENDC)
    print(f"{operation*16}")
