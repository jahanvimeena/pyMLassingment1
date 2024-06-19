# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters in both strings and compare
    return sorted(str1) == sorted(str2)

# Taking input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Checking if the strings are anagrams
if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams of each other.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams of each other.")
