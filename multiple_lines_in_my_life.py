with open("mylife.txt","w") as file:

    while True:
        enter_line = input("Enter Line: ")
        file.write(enter_line + "\n")
        more_lines = input("Are there more lines y/n? ")

        if more_lines.lower() != 'y':
            break

print("The text has written into the file of 'mylife.txt'.")
