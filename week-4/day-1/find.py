
students = [
    {'name': 'Tibi', 'age': 8},
    {'name': 'Adorjan', 'age': 9},
    {'name': 'Agoston', 'age': 6},
    {'name': 'Aurel', 'age': 7},
    {'name': 'Dezso', 'age': 12}
]

student_names_least_8 = []

students_ages_starting_with_A = []

for i in students:
    if i['age'] >= 8:
        student_names_least_8.append(i['name'])

print(student_names_least_8)

for i in students:
    if i['name'][0] == 'A':
        students_ages_starting_with_A.append(i['age'])

print(students_ages_starting_with_A)
