#Write a python program that calculates the sum of the digits of a given
#number.
# Taking input from the user
try:
    number = int(input("Enter a number: "))
    
    # Ensure the number is positive
    if number < 0:
        number = -number
    
    # Initializing the sum
    sum_of_digits = 0
    
    # Calculating the sum of the digits
    while number > 0:
        digit = number % 10
        sum_of_digits += digit
        number //= 10
    
    # Printing the result
    print(f"The sum of the digits is: ",sum_of_digits)

except ValueError:
    print("Invalid input. Please enter an integer.")
