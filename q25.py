# Function to copy contents of one file to another
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        
        with open(destination_file, 'w') as dest:
            dest.write(content)
            
        print(f"Contents copied from {source_file} to {destination_file}")
    except FileNotFoundError:
        print(f"The file '{source_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
if __name__ == "__main__":
    # Taking file names as input from the user
    source_file = input("Enter the name of the source file: ")
    destination_file = input("Enter the name of the destination file: ")
    
    # Copying the contents
    copy_file(source_file, destination_file)
