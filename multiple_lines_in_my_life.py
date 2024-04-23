with open("mylife.txt","w") as file:

    while True:
        enter_line = input("Enter Line: ")
        file.write(enter_line + "\n")
