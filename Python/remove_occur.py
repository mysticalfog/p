# File paths
input_file_path = 'input.txt'  # File to read from
output_file_path = 'output.txt'  # File to write modified content to

# Prompt the user to enter the word to remove
word_to_remove = input("Enter the word you want to remove from the file: ")

try:
    # Open the input file in read mode
    with open(input_file_path, 'r') as input_file:
        content = input_file.read()  # Read the entire content of the file

    # Remove all occurrences of the specified word
    modified_content = content.replace(word_to_remove, '')  # Replace the word with an empty string

    # Open the output file in write mode
    with open(output_file_path, 'w') as output_file:
        output_file.write(modified_content)  # Write the modified content to the output file

    # Print success message and display modified content
    print(f"All occurrences of the word '{word_to_remove}' have been removed.")
    print("\nModified Content:")
    print(modified_content)

except FileNotFoundError:
    print(f"Error: The file '{input_file_path}' was not found.")
except IOError:
    print("Error: An IOError occurred while handling the file.")