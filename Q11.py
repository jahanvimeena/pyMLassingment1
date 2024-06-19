#Write a python program that generates the first n numbers in the
#Fibonacci sequence.
# Taking input from the user
try:
    n = int(input("Enter the number of Fibonacci numbers to generate: "))

    if n <= 0:
        print("Please enter a positive integer.")
    else:
        # Initializing the first two numbers in the Fibonacci sequence
        a, b = 0, 1
        
        print("The first", n, "numbers in the Fibonacci sequence are:")
        
        # Generating and printing the Fibonacci sequence
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
except ValueError:
    print("Invalid input. Please enter an integer.")
