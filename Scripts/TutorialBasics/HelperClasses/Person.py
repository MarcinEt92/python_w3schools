class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"

    def is_adult(self):
        if self.age >= 18:
            return True
        return False

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}, grade: {self.grade}"