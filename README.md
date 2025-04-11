Task - 1  Read a file and handle errors
First create a new .txt file by the name of 'sample.txt' and feed -
'This is a sample text file.
It contains multiple lines.'
To just read the file - try:
    file = open('sample.txt', 'r') - 'r' to read
 To print command 'Reading file content:' - print("Reading file content:")
 line_num = 1
    for line in file:
        print(f"Line {line_num}: {line.strip()}")
        line_num += 1
    file.close()
    to print different lines in text file as different lines in output with Line 1, Line 2, etc
To show error if file not found - 
except FileNotFoundError:
    print("Error: 'sample.txt' was not found.")


Task - 2   Write and append data to a file
First create a new .txt file by the name of 'output.txt'
To enter first value or write in the file - 
start_input = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(start_input + "\n")
print a message - print("Data successfully written to output.txt\n")  - \n to leave blank line

To edit or say append in output.txt - 
append_input = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_input + "\n")
    print("Data successfully appended\n")

To show final output having both the lines - 
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip()) - line.strip() to show in 2 different lines, not in a single line


