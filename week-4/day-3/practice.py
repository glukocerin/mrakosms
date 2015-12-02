students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]

def count_rich_stud(students):
    summa = 0
    for student in students:
        if student['candies'] > 4:
            summa += 1

    return summa

print(count_rich_stud(students))


def count_rich_stud_filter(students):
    return len(list(filter(lambda x: x['candies'] > 4, students)))


print(count_rich_stud_filter(students))
