# Function to check if a string starts with a given prefix or ends with a given suffix
def check_prefix_suffix(input_string, prefix, suffix):
    starts_with_prefix = input_string.startswith(prefix)
    ends_with_suffix = input_string.endswith(suffix)
    return starts_with_prefix, ends_with_suffix

# Taking input from the user
input_string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

# Checking if the string starts with the prefix or ends with the suffix
starts_with_prefix, ends_with_suffix = check_prefix_suffix(input_string, prefix, suffix)

# Printing the results
if starts_with_prefix:
    print(f"The string starts with the prefix '{prefix}'.")
else:
    print(f"The string does not start with the prefix '{prefix}'.")

if ends_with_suffix:
    print(f"The string ends with the suffix '{suffix}'.")
else:
    print(f"The string does not end with the suffix '{suffix}'.")
