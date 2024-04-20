with open("student_gwa.txt","r") as file:
    datas = file.readlines()

highest_general_weighted_average = float('inf')
name_student = ''

for data in datas:
    name, general_weighted_average = data.strip().split(',')
    general_weighted_average = float(general_weighted_average)

    if general_weighted_average <= highest_general_weighted_average:
