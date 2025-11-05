class Student:
    def __init__(self, fio, age, group_number, average_grade):
        self.fio = fio
        self.age = age
        self.group_number = group_number
        self.average_grade = average_grade

    def show_info(self):
        print(f"ФИО: {self.fio}")
        print(f"Возраст: {self.age}")
        print(f"Номер группы: {self.group_number}")
        print(f"Средний балл: {self.average_grade}")

    def get_scholarship(self):
        if self.average_grade == 5:
            return 6000
        elif self.average_grade < 5:
            return 4000
        else:
            return 0

    def compare_scholarship(self, other):
        my_scholarship = self.get_scholarship()
        other_scholarship = other.get_scholarship()

        if my_scholarship > other_scholarship:
            print(f"{self.fio} получает стипендию больше, чем {other.fio}.")
        elif my_scholarship < other_scholarship:
            print(f"{self.fio} получает стипендию меньше, чем {other.fio}.")
        else:
            print(f"{self.fio} и {other.fio} получают одинаковую стипендию.")


class Postgraduate(Student):
    def __init__(self, fio, age, group_number, average_grade, research_work):
        super().__init__(fio, age, group_number, average_grade)
        self.research_work = research_work

    def show_info(self):
        super().show_info()
        print(f"Научная работа: {self.research_work}")

    def get_scholarship(self):
        if self.average_grade == 5:
            return 8000
        elif self.average_grade < 5:
            return 6000
        else:
            return 0


# test part
student1 = Student("Иванов Иван", 20, "101/2", 5)
student2 = Postgraduate("Петров Петр", 25, "201/3", 4.5, "Исследование ИИ")

print("Информация о студенте:")
student1.show_info()
print(f"Стипендия: {student1.get_scholarship()} руб.\n")

print("Информация об аспиранте:")
student2.show_info()
print(f"Стипендия: {student2.get_scholarship()} руб.\n")

student1.compare_scholarship(student2)
