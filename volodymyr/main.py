from datetime import datetime
from personnel_manager import PersonnelManager

def validate_name(name):
    return name.isalpha() and name[0].isupper() and len(name) >= 2

def validate_hire_date(hire_date_str):
    try:
        hire_date = datetime.strptime(hire_date_str, "%Y-%m-%d")
        return hire_date <= datetime.now()
    except ValueError:
        return False

def main():
    manager = PersonnelManager()
    allowed_access_levels = ['junior', 'middle', 'senior', 'lead']

    while True:
        print("\nМеню:")
        print("1. Додати нову посаду")
        print("2. Додати співробітника")
        print("3. Переглянути співробітників")
        print("4. Видалити співробітника")
        print("5. Оновити інформацію про співробітника")
        print("6. Підрахувати загальну зарплату")
        print("7. Вийти")
        choice = input("Оберіть дію: ")

        if choice == "1":
            title = input("Назва посади: ")
            access_level = input("Рівень доступу (junior, middle, senior, lead): ").lower()

            if access_level not in allowed_access_levels:
                print("❌ Некоректний рівень доступу!")
                continue

            try:
                base_salary = float(input("Базова зарплата: "))
                if base_salary <= 0:
                    raise ValueError
            except ValueError:
                print("❌ Некоректна зарплата!")
                continue

            manager.add_position(title, access_level, base_salary)

        elif choice == "2":
            first_name = input("Ім'я: ")
            last_name = input("Прізвище: ")

            if not (validate_name(first_name) and validate_name(last_name)):
                print("❌ Некоректне ім’я або прізвище!")
                continue

            position_title = input("Посада: ")
            hire_date_str = input("Дата прийняття на роботу (yyyy-mm-dd): ")

            if not validate_hire_date(hire_date_str):
                print("❌ Некоректна дата прийняття на роботу!")
                continue

            hire_date = datetime.strptime(hire_date_str, "%Y-%m-%d")

            try:
                salary = float(input("Зарплата: "))
                if salary <= 0:
                    raise ValueError
            except ValueError:
                print("❌ Некоректна зарплата!")
                continue

            manager.add_employee(first_name, last_name, position_title, hire_date, salary)

        elif choice == "3":
            sort_by = input("За яким критерієм сортувати (first_name, last_name, hire_date): ")
            manager.view_employees(sort_by)

        elif choice == "4":
            first_name = input("Ім'я співробітника для видалення: ")
            last_name = input("Прізвище співробітника для видалення: ")
            manager.remove_employee(first_name, last_name)

        elif choice == "5":
            first_name = input("Ім'я співробітника для оновлення: ")
            last_name = input("Прізвище співробітника для оновлення: ")
            new_position = input("Нова посада (залиште порожнім, якщо не потрібно): ")
            new_salary = input("Нова зарплата (залиште порожнім, якщо не потрібно): ")

            if new_salary:
                try:
                    new_salary = float(new_salary)
                    if new_salary <= 0:
                        raise ValueError
                except ValueError:
                    print("❌ Некоректна зарплата!")
                    continue
            else:
                new_salary = None

            manager.update_employee(first_name, last_name, new_position, new_salary)

        elif choice == "6":
            manager.calculate_total_salary()

        elif choice == "7":
            print("До побачення!")
            break

if __name__ == "__main__":
    main()
