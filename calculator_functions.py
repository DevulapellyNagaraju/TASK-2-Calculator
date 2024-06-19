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

    print(f"\n  {num1}" )
    print( f"{operation} {num2}" )
    print(f"{operation*16}")
    print(f" Answer: {result}\n" )
    print(f"{operation*16}")
