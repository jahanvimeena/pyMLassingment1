# Function to find the minimum and maximum values in a list of numbers
def find_min_max(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    return min_value, max_value

# Taking input from the user and converting it to a list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = [float(num) for num in user_input.split()]

# Finding the minimum and maximum values
min_value, max_value = find_min_max(numbers_list)

# Printing the result
print(f"The minimum value in the list is: {min_value}")
print(f"The maximum value in the list is: {max_value}")
