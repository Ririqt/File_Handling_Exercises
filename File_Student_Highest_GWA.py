with open("student_gwa.txt","r") as file:
    datas = file.readlines()

highest_general_weighted_average = float('inf')
name_student = ''

for data in datas:
