# Specify the input and output file paths
input_file_path = 'input.txt'  # File to read from
output_file_path = 'output.txt'  # File to write reversed content to

try:
    # Open the input file in read mode
    with open(input_file_path, 'r') as input_file:
        content = input_file.read()  # Read the entire content of the file

    # Reverse the content
    reversed_content = content[::-1]  # Reverse the string

    # Open the output file in write mode
    with open(output_file_path, 'w') as output_file:
        output_file.write(reversed_content)  # Write the reversed content to the output file

    print(f"Reversed content has been written to '{output_file_path}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_file_path}' was not found.")
except IOError:
    print("Error: An IOError occurred while handling the file.")