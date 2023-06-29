class Vehicle:
    def __init__(self, brand="Unknown Brand", model="Unknown Model"):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} - {self.model}"

    def move(self):
        print("Drive")

class Plane(Vehicle):
    def __init__(self, brand="Unknown Brand", model="Unknown Model", number_of_wings=2):
        super().__init__(brand, model)
        self.number_of_wings = number_of_wings

    def move(self):
        print("Fly")