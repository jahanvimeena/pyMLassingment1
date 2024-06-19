# Function to convert a string into a list of its characters
def string_to_char_list(input_string):
    return list(input_string)

# Taking input from the user
user_input = input("Enter a string: ")

# Converting the string to a list of characters
char_list = string_to_char_list(user_input)

# Printing the result
print("The list of characters is:", char_list)
