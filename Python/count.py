def count_file_contents(filenames):
    """
    Counts the lines, words, and characters in each file provided in the list.

    :param filenames: List of filenames to process
    """
    for filename in filenames:
        try:
            # Open the file in read mode
            with open(filename, 'r') as file:
                lines = file.readlines()  # Read all lines in the file
                
                # Count the number of lines, words, and characters
                line_count = len(lines)
                word_count = sum(len(line.split()) for line in lines)
                char_count = sum(len(line) for line in lines)

                # Print the counts for the current file
                print(f"File: {filename}")
                print(f"Lines: {line_count}")
                print(f"Words: {word_count}")
                print(f"Characters: {char_count}")
                print("-" * 30)  # Separator line for readability

        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except IOError:
            print(f"Error: An IOError occurred while reading '{filename}'.")


# Example usage
file_list = ["file1.txt", "file2.txt", "file3.txt"]  # List of files to process
count_file_contents(file_list)