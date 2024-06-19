# Function to calculate the sum of a list of numbers
def sum_of_numbers(numbers):
    return sum(numbers)

# Taking input from the user and converting it to a list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = [float(num) for num in user_input.split()]

# Calculating the sum of the numbers
total_sum = sum_of_numbers(numbers_list)

# Printing the result
print(f"The sum of the numbers is: {total_sum}")
