#Write a python program that checks whether a given number is even or
#odd.

number = int(input("Enter a number: "))


if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
