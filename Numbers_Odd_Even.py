# Reading Numbers into the numbers.txt
with open("numbers.txt", "r") as file:
    numbers = file.read().split()

# Storing numbers making num 'int'
numbers = [int(num) for num in numbers]

# Even and Odd Numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Creating Even File Numbers
with open("even_numbers.txt", "w") as even_file:
    for num in even_numbers:
        even_file.write(str(num) + "\n")

# Creating Odd File Numbers
with open("odd_numbers.txt", "w") as odd_file:
    for num in odd_numbers:
        odd_file.write(str(num) + "\n")
