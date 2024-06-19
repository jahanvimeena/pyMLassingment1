import string

# Function to remove punctuation from a string
def remove_punctuation(input_string):
    # Create a translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

# Taking input from the user
user_input = input("Enter a string: ")

# Removing punctuation from the string
cleaned_string = remove_punctuation(user_input)

# Printing the result
print(f"The string without punctuation is: {cleaned_string}")
