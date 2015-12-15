class Student:
    def __init__(self):
        self.grade = []

    def add_grade(self, grade):
        self.grade.append(grade)

    def get_average(self):
        return round(sum(self.grade) / len(self.grade), 2)



akos = Student()
akos.add_grade(5)
akos.add_grade(4)
akos.add_grade(4)

print(akos.get_average())
