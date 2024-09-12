import re
import os

class UniqueIntegers:
    @staticmethod
    def processFile(inputFilePath: str, outputFilePath: str):
        unique_integers = set()  # This removes duplicates

        # Open and read the input file
        with open(inputFilePath, 'r') as infile:
            for line in infile:
                line = line.strip()  # To remove spaces
                if line:
                    match = re.fullmatch(r'^-?\d+$', line)  # Match a single integer
                    if match:
                        number = int(match.group())  # Convert string to integer
                        unique_integers.add(number)  # Add to set (automatically removes duplicates)

        # Sort the unique integers
        sorted_unique_integers = sorted(unique_integers)

        # Write sorted integers to the output file
        with open(outputFilePath, 'w') as outfile:
            for number in sorted_unique_integers:
                outfile.write(f"{number}\n")  # Write each integer on a new line

# Main part of the script
if __name__ == "__main__":
    input_directory = 'C:/Users/LENOVO/OneDrive/Desktop/DSA-HW01-UniqueInt/dsa/how01/sample_inputs'
    output_directory = 'C:/Users/LENOVO/OneDrive/Desktop/DSA-HW01-UniqueInt/dsa/how01/sample_results'

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Process each .txt file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):  # Only process .txt files
            input_path = os.path.join(input_directory, filename)
            output_filename = f"{filename}_results.txt"
            output_path = os.path.join(output_directory, output_filename)

            # Process the file using the UniqueIntegers class
            UniqueIntegers.processFile(input_path, output_path)
