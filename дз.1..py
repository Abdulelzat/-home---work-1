
class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marital_status = "женат" if self.is_married else "не женат"
        print(f"Меня зовут {self.full_name}, мне {self.age} лет, я {marital_status}.")

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_grade(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

class Teacher(Person):
    def __init__(self, full_name, age, is_married, experience, base_salary):
        super().__init__(full_name, age, is_married)
        self.experience = experience
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus = 0.05 * max(0, self.experience - 3)
        return self.base_salary * (1 + bonus)

def create_students():
    students = [
        Student("Камбаров Айжигит", 19, False, {"Математика": 5, "Физика": 4, "История": 3}),
        Student("Алыкулов Чынтемир", 18, False, {"Математика": 4, "Физика": 5, "История": 5}),
        Student("Акпаралиев Кутман", 17, False, {"Математика": 3, "Физика": 4, "История": 2}),
    ]
    return students

# Создание объекта учителя
teacher = Teacher("Элзат Толонов", 29, True, 5, 50000)

# Печать информации о учителе и расчет зарплаты
teacher.introduce_myself()
print(f"Опыт: {teacher.experience} лет")
print(f"Зарплата: {teacher.calculate_salary()}")

# Создание учеников и вывод их информации
students = create_students()
for student in students:
    student.introduce_myself()
    print("Оценки:", student.marks)
    print("Средняя оценка:", student.average_grade())
    print()  # Для удобства читаемости
