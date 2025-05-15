class Position:
    ALLOWED_ACCESS_LEVELS = ["junior", "middle", "senior", "lead"]

    def __init__(self, title, access_level, salary):
        """Ініціалізація об'єкта посади."""
        self.title = title
        self.access_level = access_level
        self.salary = salary

        # Перевірка рівня доступу
        if not self.is_valid_access_level(access_level):
            raise ValueError(f"Невірний рівень доступу: {access_level}. Дозволені рівні доступу: {', '.join(self.ALLOWED_ACCESS_LEVELS)}")

    def is_valid_access_level(self, access_level):
        """Перевірка, чи є рівень доступу дозволеним для компанії."""
        return access_level.lower() in self.ALLOWED_ACCESS_LEVELS
