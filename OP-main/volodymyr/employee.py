from datetime import datetime
from position import Position

class Employee:
    def __init__(self, first_name, last_name, position, hire_date, salary):
        """Ініціалізація співробітника."""
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.hire_date = hire_date
        self.salary = salary

    def __str__(self):
        """Виведення співробітника в зручному форматі."""
        return f"{self.first_name} {self.last_name}, {self.position.title}, {self.hire_date}, {self.salary}"
