# List to store the lines of input
lines = []

print("Enter multiple lines of text. Press Enter on an empty line to finish:")

# Reading lines until an empty line is entered
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

# Printing all the lines
print("\nYou entered:")
for line in lines:
    print(line)
