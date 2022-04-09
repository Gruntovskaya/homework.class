class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.middle_grade = []

    def rate_lecturers(self, lecturer, course, grade):
        if course in lecturer.course:
            if grade <= 10:
                lecturer.grades[course] = lecturer.grades.get(course, []) + [grade]

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
        return f'Lecturer:\nИмя:{self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.middle_grades}'



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

student = Student('Ruoy', 'Eman', 'your_gender')
student.courses_in_progress += ['Python']
student2 = Student('Иван', 'Иванов', 'Муж')
student2.courses_in_progress += ['Python']

mentor = Reviewer('Some', 'Buddy')
mentor.courses_attached += ['Python']

mentor.rate_hw(student, 'Python', 10)
mentor.rate_hw(student, 'Python', 10)
mentor.rate_hw(student, 'Python', 5)

mentor.rate_hw(student2, 'Python', 5)
mentor.rate_hw(student2, 'Python', 6)
mentor.rate_hw(student2, 'Python', 10)

lecturer = Lecturer('Герман','Гетц','Python')
lecturer2 = Lecturer('Георгий','Бентовский','Java')
student.rate_lecturers(lecturer2,'Java',7)
student.rate_lecturers(lecturer,'Python',8)
student.rate_lecturers(lecturer,'Python',10)
student.rate_lecturers(lecturer2,'Java',5,)


# print('Студент: ',best_student2.name,best_student2.surname)
# print('Оценки студентов: ',cool_lecturer.grades,'Преподаватель: ',cool_lecturer.name,cool_lecturer.surname)
student.finished_courses = 'Git'
student.middle_grade_students('Python')
student2.finished_courses = 'Java'
student2.middle_grade_students('Python')
print(student2)
print()
print(mentor)
print()
lecturer2.middle_grades_lecturers('Java')
print(lecturer2)
print()
def contrast_lecturer():
    if lecturer2.middle_grades< lecturer.middle_grades:
            print('Лучший преподаватель: ',lecturer.name, lecturer.surname)
    else:
            print('Лучший преподаватель: ',lecturer2.name, lecturer2.surname)

contrast_lecturer()
print()
def contrast_student():
    if student.middle_grade < student2.middle_grade:
        print('Лучший студент: ', student2.name, student2.surname)
    else:
        print('Лучший студент: ', student.name, student.surname)
contrast_student()
print()

def middle_grades_students():
    u = round(sum(student.middle_grade+student2.middle_grade) / 2, 1)
    print('Средняя оценка за домашние задания по всем студентам: ', u)

middle_grades_students()
print()
def middle_grades_lecturer():
    q = round(sum(lecturer.middle_grades+lecturer2.middle_grades) / 2, 1)
    print('Средняя оценка за лекции по всем лекторам: ', q)

middle_grades_lecturer()