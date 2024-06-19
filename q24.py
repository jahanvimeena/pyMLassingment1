# Function to perform the calculation
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator!"

# Main program
if __name__ == "__main__":
    try:
        # Taking input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        
        # Performing the calculation
        result = calculate(num1, num2, operator)
        
        # Printing the result
        print(f"The result of {num1} {operator} {num2} is: {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
