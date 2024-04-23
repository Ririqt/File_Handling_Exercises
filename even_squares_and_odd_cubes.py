with open("integers.txt", 'r') as file:
    integers = [int(line.strip()) for line in file]

even_integers = [number for number in integers if number % 2 == 0]
odd_integers = [number for number in integers if number % 2 != 0]

even_squares = [number ** 2 for number in even_integers]
