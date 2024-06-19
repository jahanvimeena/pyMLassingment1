# Function to count the occurrences of a specific element in a list
def count_occurrences(lst, element):
    return lst.count(element)

# Taking input from the user and converting it to a list of elements
user_input = input("Enter a list of elements separated by spaces: ")
elements_list = user_input.split()

# Taking the specific element to count its occurrences
element_to_count = input("Enter the element to count its occurrences: ")

# Counting the occurrences of the specific element
occurrences = count_occurrences(elements_list, element_to_count)

# Printing the result
print(f"The element '{element_to_count}' occurs {occurrences} times in the list.")
