with open("numbers.txt", "r") as file:
    numbers = file.read().split()

numbers = [int(num) for num in numbers]

even_numbers = [num for num in numbers if num % 2 == 1]