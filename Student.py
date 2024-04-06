from statistics import mean
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_course(self, lector, course, grade):
        if isinstance(lector, Lecturer) and (course in self.finished_courses or course in self.courses_in_progress) and\
                course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__sravni()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def __sravni(self):
        mean_score = []
        for i in self.grades.values():
            mean_score += i
        if mean_score == []:
            mean_score = 0
        else:
            mean_score = mean(mean_score)
        return mean_score

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__sravni() == other.__sravni()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.__sravni() < other.__sravni()
        return False

    def __le__(self, other):
        if isinstance(other, Student):
            return self.__sravni() <= other.__sravni()
        return False

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.__sravni() > other.__sravni()
        return False

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.__sravni() >= other.__sravni()
        return False

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__sravni()}'

    def __sravni(self):
        mean_score = []
        for i in self.grades.values():
            mean_score += i
        if mean_score == []:
            mean_score = 0
        else:
            mean_score = mean(mean_score)
        return mean_score

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.__sravni() == other.__sravni()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.__sravni() < other.__sravni()
        return False

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.__sravni() <= other.__sravni()
        return False

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.__sravni() > other.__sravni()
        return False

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.__sravni() >= other.__sravni()
        return False

class Potok_studets:
    def __call__(self, students, course):
        mean_score = []
        for i in students:
            if isinstance(i, Student) and course in i.grades:
                mean_score += i.grades[course]
        if mean_score:
            mean_score = mean(mean_score)
        else:
            mean_score = 0
        return mean_score

class Potok_lectors:
    def __call__(self, lectors, course):
        mean_score = []
        for i in lectors:
            if isinstance(i, Lecturer) and course in i.grades:
                mean_score += i.grades[course]
        if mean_score:
            mean_score = mean(mean_score)
        else:
            mean_score = 0
        return mean_score



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student_2 = Student('LOx', 'Pedalni', 'pidr')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['PHP']
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['PHP']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'PHP', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student_2, 'Python', 2)
cool_mentor.rate_hw(best_student_2, 'Python', 5)
cool_mentor.rate_hw(best_student_2, 'PHP', 7)
#
# print(best_student.grades)

reviewer = Reviewer('Boris', 'Britva')
# print(reviewer.name, reviewer.surname)

reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['PHP']
# print(reviewer.courses_attached)

reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 3)
reviewer.rate_hw(best_student, 'PHP', 10)
reviewer.rate_hw(best_student_2, 'Python', 8)
reviewer.rate_hw(best_student_2, 'PHP', 8)
reviewer.rate_hw(best_student_2, 'Python', 10)
# print(best_student.grades)

lector = Lecturer('Alah', 'Babah')
lector.courses_attached += ['Python']
lector.courses_attached += ['PHP']
lector_2 = Lecturer('Neto', 'Logy')
lector_2.courses_attached += ['Python']
lector_2.courses_attached += ['PHP']
# print(lector.courses_attached)

best_student.rate_course(lector, 'Python', 2)
best_student.rate_course(lector, 'Python', 3)
best_student.rate_course(lector, 'PHP', 1)
best_student_2.rate_course(lector, 'PHP', 6)
best_student_2.rate_course(lector, 'Python', 3)
best_student_2.rate_course(lector, 'Python', 4)
best_student_2.rate_course(lector_2, 'PHP', 3)
best_student_2.rate_course(lector_2, 'Python', 6)
best_student_2.rate_course(lector_2, 'Python', 1)
best_student.rate_course(lector_2, 'Python', 9)
best_student.rate_course(lector_2, 'Python', 10)
best_student.rate_course(lector_2, 'PHP', 3)
# print(lector.grades)

# print(reviewer)
# print(best_student)
# print(lector)
potok_studets = Potok_studets()
# print(potok_studets([best_student,best_student_2],'Python'))
# print(best_student.grades,best_student_2.grades)
potok_lectors = Potok_lectors()
print(potok_lectors([lector, lector_2], 'Python'))
print(lector.grades,lector_2.grades)