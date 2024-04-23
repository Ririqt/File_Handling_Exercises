# Writing into the File
with open("mylife.txt","w") as file:

# Creating a Loop for Entering Lines
    while True:
        enter_line = input("Enter Line: ")
        file.write(enter_line + "\n")
        more_lines = input("Are there more lines y/n? ")

        # Exiting the Loop
        if more_lines.lower() != 'y':
            break

# Display of Success Text
print("The text has written into the file of 'mylife.txt'.")
