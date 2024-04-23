with open("integers.txt", 'r') as file:
    integers = [int(line.strip()) for line in file]

even_integers = [number for number in integers if number % 2 == 0]
odd_integers = [number for number in integers if number % 2 != 0]

even_squares = [number ** 2 for number in even_integers]
odd_cubes = [number ** 3 for number in odd_integers]

with open('double.txt', 'w') as file:
    for square in even_squares:
        file.write(f"{square}\n")
