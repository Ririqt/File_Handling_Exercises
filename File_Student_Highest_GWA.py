# Reading Per Line in the Files' Data
with open("students_gwa.txt","r") as file:
    datas = file.readlines()

# Storing the Data
highest_general_weighted_average = float('inf')
name_student = ''

# Separating the Data from the file
for data in datas:
    name, general_weighted_average = data.strip().split(',')
    general_weighted_average = float(general_weighted_average)

# Getting the Highest General Weighted Average
    if general_weighted_average <= highest_general_weighted_average:
        highest_general_weighted_average = general_weighted_average
        name_student = name

# Displaying the Student who got the highest GWA
print(f"The highest GWA is '{highest_general_weighted_average}' which is student '{name_student}'!")
