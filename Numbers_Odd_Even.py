with open("numbers.txt", "r") as file:
    numbers = file.read().split()

numbers = [int(num) for num in numbers]
