import doctest

"""Class BankAccount
Класс для создания банковского счета с определенным балансов
Из функционала: deposit и withdraw, которые вносят и снимают деньги со счета соответственно
Пример:
Owner_1 = BankAccount("Иванов", 500) - создание счета на имя Иванова со счетом 500
Owner_1.deposit(250) - вносит на баланс 250, вывод покажет 750
Owner_1.withdraw(400) - выводит с баланса 400, вывод покажет 350"""

"""class Car
Класс создает машину определенной марки с определенной скоростью
Из функционала: Увеличение и уменьшение скорости созданной машины - accelerate и brake соответственно
Пример:
Car_1 = Car("Renault", 60) - создание авто Renault со скоростью 60
Car_1.accelerate(10) - увеличиваем скорость на 10, вывод - 70
Car_1.break(30) - сбрасываем скорость до 40"""

"""class Laptop
Создание ноутбука определенного бренда с каким-то количеством оперативной и постоянной памяти
Из функционала: Увеличение объема постоянной памяти или RAM
Пример:
Laptop_1 = Laptop("Lenovo", 8, 500) - ноутбук Lenovo с RAM = 8 и HDD = 500
Laptop_1.upgrade_ram(16) - добавляем в ноутбук оперативную память
"""

"""В каждом классе:
 с помощью :raise: вызывалась ошибка, если подаются некорректные данные на вход
 Также осуществлялась проверка в функциях увеличений значений - не вводится ли отрицательное число
 В классе используется три функции с различным назначением, где начальная
 :__init__: устанавливает параметры входных данных
 Также в class входит self, что означает наличие "имени" у каждого созданного объекта
 """


class BankAccount:
    def __init__(self, owner: str, balance: float):
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным.")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Вносит деньги на счёт.

        :param amount: Сумма пополнения (должна быть положительной).
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount: float) -> float:
        """
        Снимает деньги со счёта.

        :param amount: Сумма снятия (не больше текущего баланса).
        :return: Оставшийся баланс.
        """
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счёте.")
        self.balance -= amount
        return self.balance


class Car:
    def __init__(self, brand: str, speed: int):
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной.")
        self.brand = brand
        self.speed = speed

    def accelerate(self, increase: int) -> int:
        """
        Увеличивает скорость машины.

        :param increase: Значение, на которое увеличивается скорость.
        :return: Новая скорость машины.
        """
        if increase < 0:
            raise ValueError("Увеличение скорости должно быть положительным.")
        self.speed += increase
        return self.speed

    def brake(self, decrease: int = 10) -> int:
        """
        Уменьшает скорость машины.

        :param decrease: Значение, на которое уменьшается скорость (по умолчанию 10).
        :return: Новая скорость машины.
        """
        if decrease < 0:
            raise ValueError("Уменьшение скорости должно быть положительным.")
        self.speed = max(0, self.speed - decrease)
        return self.speed


class Laptop:
    def __init__(self, brand: str, ram: int, storage: int):
        if ram <= 0 or storage <= 0:
            raise ValueError("Оперативная память и накопитель должны быть положительными числами.")
        self.brand = brand
        self.ram = ram  # ОЗУ в ГБ
        self.storage = storage  # Память в ГБ

    def upgrade_ram(self, additional_ram: int) -> int:
        """
        Увеличивает объём оперативной памяти.

        :param additional_ram: Количество ГБ, на которое увеличивается ОЗУ.
        :return: Новый объём ОЗУ.

        >>> laptop = Laptop("Lenovo", 8, 500)
        >>> laptop.upgrade_ram(16)
        24
        """
        if additional_ram <= 0:
            raise ValueError("Дополнительная память должна быть положительной.")
        self.ram += additional_ram
        return self.ram

    def upgrade_storage(self, additional_storage: int = 256) -> int:
        """
        Увеличивает объём накопителя.

        :param additional_storage: Количество ГБ, на которое увеличивается память (по умолчанию 256 ГБ).
        :return: Новый объём памяти.

        >>> laptop = Laptop("HP", 16, 512)
        >>> laptop.upgrade_storage()
        768
        >>> laptop.upgrade_storage(128)
        896
        """
        if additional_storage <= 0:
            raise ValueError("Дополнительная память должна быть положительной.")
        self.storage += additional_storage
        return self.storage

if __name__ == "__main__":
    doctest.testmod()