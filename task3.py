class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.middle_grade = []

    def rate_lecturers(self, course, grade):
        if course in cool_lecturer.course:
            if grade <= 10:
                cool_lecturer.grades[course] = cool_lecturer.grades.get(course, []) + [grade]

    def middle_grade_students(self, course):
        self.middle_grade.append(round(int(sum(self.grades.get(course))) / len(self.grades.get(course)), 1))
        return self.middle_grade

    def __str__(self):
        return f'Student:\nИмя:{self.name}\nФамилия: {self.surname}\nСредняя оценка за ДЗ: {self.middle_grade}' \
               f'\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}' \
               f'\nЗавершенные курсы: {"".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, course):
        super().__init__(name, surname)
        self.course = course
        self.grades = {course: []}
        self.middle_grades = []
    def middle_grades_lecturers(self, course):
        self.middle_grades.append(round(int(sum(self.grades.get(course))) / len(self.grades.get(course)), 1))
        return self.middle_grades
    def __str__(self):
        return f'Lecturer:\nИмя:{self.name}\nФамилия: {self.surname}\nСредняя оценка за ДЗ: {self.middle_grades}'



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Reviewer: \n Имя:{self.name}\n Фамилия: {self.surname}'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 5)

cool_lecturer = Lecturer('Герман','Гетц','Python')
best_student2 = Student('Иван', 'Иванов', 'Муж')
best_student.rate_lecturers('jawa',10)
best_student.rate_lecturers('Python',8)
best_student.rate_lecturers('Python',10)

# print('Студент: ',best_student2.name,best_student2.surname)
# print('Оценки студентов: ',cool_lecturer.grades,'Преподаватель: ',cool_lecturer.name,cool_lecturer.surname)
best_student.finished_courses = 'Git'
best_student.middle_grade_students('Python')
print(best_student)
print()
print(cool_mentor)
print()
cool_lecturer.middle_grades_lecturers('Python')
print(cool_lecturer)
