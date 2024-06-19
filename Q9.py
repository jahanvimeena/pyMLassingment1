#Write a python program that checks if a substring is present in a given
#string.
# Taking input from the user
main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")

# Checking if the substring is present in the main string
if substring in main_string:
    print(f"The substring ", substring,  "is present in the main string.")
else:
    print(f"The substring " ,substring, " is not present in the main string.")
