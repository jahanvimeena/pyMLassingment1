#from datetime import datetime

# Taking input from the user
try:
    birth_year = int(input("Enter your birth year: "))

    # Getting the current year
    current_year = datetime.now().year

    # Calculating the age
    age = current_year - birth_year

    # Printing the result
    print(f"You are {age} years old.")

except ValueError:
    print("Invalid input. Please enter a valid year.")
