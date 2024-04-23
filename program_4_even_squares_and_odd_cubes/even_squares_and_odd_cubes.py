# Reading the File
with open("integers.txt", 'r') as file:
    integers = [int(line.strip()) for line in file]

# Getting the Even Integers
even_integers = [number for number in integers if number % 2 == 0]

# Getting the Odd Integers
odd_integers = [number for number in integers if number % 2 != 0]

# Calculate the Even Squares
even_squares = [number ** 2 for number in even_integers]

# Calculate the Odd Cubes
odd_cubes = [number ** 3 for number in odd_integers]

# Creating the Even Squares File
with open("double.txt", "w") as file:
    for square in even_squares:
        file.write(f"{square}\n")

# Creating the Odd Cubes File
with open("triple.txt", "w") as file:
    for cube in odd_cubes:
        file.write(f"{cube}\n")

# Display the Success Text
print("The file of Even Numbers in 'double.txt' and Odd Numbers in 'triple.txt' were successfully created.")
