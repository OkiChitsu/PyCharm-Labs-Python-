from task_1 import BankAccount, Car, Laptop
#Был подправлен файл task_1 т.к. код из первого задания копировался некорректно
if __name__ == "__main__":
    account = BankAccount("Alice", 1000)
    car = Car("Toyota", 60)
    laptop = Laptop("Dell", 16, 512)

    try:
        # Попытка снять больше денег, чем есть на счете
        account.withdraw(2000)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        # Попытка увеличить скорость на отрицательное значение
        car.accelerate(-10)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        # Попытка добавить отрицательный объем памяти
        laptop.upgrade_ram(-4)
    except ValueError:
        print('Ошибка: неправильные данные')