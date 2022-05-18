class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = name[0] + last_name + birth_year


name_in = input()
last_name_in = input()
birth_year_in = input()

koby = Student(name_in, last_name_in, birth_year_in)
print(koby.student_id)
