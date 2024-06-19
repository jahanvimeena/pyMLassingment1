import csv

# Function to read and print CSV data
def read_csv(file_path):
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            
            # Printing the contents of the CSV file
            for row in csv_reader:
                print(', '.join(row))
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
if __name__ == "__main__":
    # Specify the path to your CSV file
    file_path = "data.csv"
    
    # Read and print the CSV data
    read_csv(file_path)
