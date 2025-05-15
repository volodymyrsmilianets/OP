from employee import Employee
from position import Position

class PersonnelManager:
    def __init__(self):
        self.positions = []
        self.employees = []

    def add_position(self, title, access_level, base_salary):
        for position in self.positions:
            if position.title.lower() == title.lower():
                print(f"❌ Посада '{title}' вже існує.")
                return
        self.positions.append(Position(title, access_level, base_salary))
        print(f"✅ Посада '{title}' успішно додана.")


    def add_employee(self, first_name, last_name, position_title, hire_date, salary):
        """Додавання нового співробітника до списку."""
        position = self.get_position_by_title(position_title)
        if position:
            employee = Employee(first_name, last_name, position, hire_date, salary)
            self.employees.append(employee)
            print(f"Співробітник {first_name} {last_name} успішно доданий!")
        else:
            print(f"Посада {position_title} не знайдена.")

    def get_position_by_title(self, title):
        """Повертає посаду за назвою або None, якщо посада не знайдена."""
        for position in self.positions:
            if position.title == title:
                return position
        return None

    def view_employees(self, sort_by="last_name"):
        """Перегляд списку співробітників, сортує за вказаним критерієм."""
        sorted_employees = sorted(self.employees, key=lambda emp: getattr(emp, sort_by, ''))
        if sorted_employees:
            for employee in sorted_employees:
                print(employee)
        else:
            print("Немає співробітників для відображення.")

    def remove_employee(self, first_name, last_name):
        """Видалення співробітника зі списку."""
        self.employees = [emp for emp in self.employees if not (emp.first_name == first_name and emp.last_name == last_name)]
        print(f"Співробітник {first_name} {last_name} видалений.")

    def update_employee(self, first_name, last_name, new_position_title=None, new_salary=None):
        """Оновлення інформації про співробітника."""
        for employee in self.employees:
            if employee.first_name == first_name and employee.last_name == last_name:
                if new_position_title:
                    new_position = self.get_position_by_title(new_position_title)
                    if new_position:
                        employee.position = new_position
                    else:
                        print(f"Посада {new_position_title} не знайдена.")
                if new_salary is not None:
                    employee.salary = new_salary
                print(f"Інформація про співробітника {first_name} {last_name} оновлена.")
                return
        print(f"Співробітник {first_name} {last_name} не знайдений.")

    def calculate_total_salary(self):
        """Підраховує загальну зарплату всіх співробітників."""
        total_salary = sum(emp.salary for emp in self.employees)
        print(f"Загальна зарплата всіх співробітників: {total_salary}")
