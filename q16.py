# Taking input from the user
user_input = input("Enter a string: ")

# Initializing an empty dictionary to store the frequency of each character
char_frequency = {}

# Counting the frequency of each character
for char in user_input:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Printing the character frequencies
print("Character frequencies:")
for char, frequency in char_frequency.items():
    print(f"{char}: {frequency}")
