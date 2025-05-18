from datetime import datetime

class Payroll:
    ACCESS_LEVEL_MULTIPLIERS = {
        'junior': 1.0,
        'middle': 1.2,
        'senior': 1.5,
        'lead': 1.8
    }

    @staticmethod
    def calculate_salary(employee):
        """Обчислює зарплату з урахуванням стажу та рівня доступу."""
        base_salary = employee.salary
        access_multiplier = Payroll.ACCESS_LEVEL_MULTIPLIERS.get(employee.position.access_level.lower(), 1.0)

        # Розрахунок стажу в повних роках
        years_worked = (datetime.now() - employee.hire_date).days // 365
        experience_bonus = 1 + (0.03 * years_worked)  # +3% за кожен рік

        final_salary = base_salary * access_multiplier * experience_bonus
        return round(final_salary, 2)
