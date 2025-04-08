start_input = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(start_input + "\n")

append_input = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_input + "\n")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())

