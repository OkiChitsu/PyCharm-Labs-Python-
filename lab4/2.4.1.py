class TransportVehicle:
    """
    Базовый класс для транспортных средств.

    Атрибуты:
        transport_type (str): тип транспортного средства
        max_speed (float): максимальная скорость (км/ч)
        capacity (int): вместимость (количество людей)
    """

    def __init__(self, transport_type: str, max_speed: float, capacity: int):
        """
        Инициализация транспортного средства.

        Args:
            transport_type: тип транспортного средства
            max_speed: максимальная скорость в км/ч
            capacity: пассажировместимость
        """
        self._transport_type = transport_type
        self._max_speed = max_speed
        self._capacity = capacity

    @property
    def transport_type(self) -> str:
        """Получить тип транспортного средства."""
        return self._transport_type

    @property
    def max_speed(self) -> float:
        """Получить максимальную скорость."""
        return self._max_speed

    @property
    def capacity(self) -> int:
        """Получить вместимость."""
        return self._capacity

    def calculate_travel_time(self, distance: float) -> float:
        """
        Рассчитать время в пути.

        Args:
            distance: расстояние в км

        Returns:
            Время в часах
        """
        return distance / self.max_speed

    def __str__(self) -> str:
        return (f"Транспортное средство типа '{self.transport_type}'. "
                f"Макс. скорость: {self.max_speed} км/ч. "
                f"Вместимость: {self.capacity} чел.")

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}("
                f"transport_type={self.transport_type!r}, "
                f"max_speed={self.max_speed!r}, "
                f"capacity={self.capacity!r})")


class Car(TransportVehicle):
    """
    Класс автомобиля, наследуется от TransportVehicle.

    Дополнительные атрибуты:
        brand (str): марка автомобиля
        fuel_consumption (float): расход топлива (л/100км)
    """

    def __init__(self, brand: str, fuel_consumption: float,
                 max_speed: float, capacity: int = 5):
        """
        Инициализация автомобиля.

        Args:
            brand: марка автомобиля
            fuel_consumption: расход топлива в л/100км
            max_speed: максимальная скорость
            capacity: вместимость (по умолчанию 5)
        """
        super().__init__("Автомобиль", max_speed, capacity)
        self._brand = brand
        self._fuel_consumption = fuel_consumption

    @property
    def brand(self) -> str:
        """Получить марку автомобиля."""
        return self._brand

    @property
    def fuel_consumption(self) -> float:
        """Получить расход топлива."""
        return self._fuel_consumption

    def calculate_travel_cost(self, distance: float, fuel_price: float) -> float:
        """
        Рассчитать стоимость поездки.

        Args:
            distance: расстояние в км
            fuel_price: цена топлива за литр

        Returns:
            Стоимость поездки
        """
        return (distance / 100) * self.fuel_consumption * fuel_price

    def calculate_travel_time(self, distance: float) -> float:
        """
        Перегруженный метод расчета времени в пути.
        Учитывает, что автомобиль не всегда едет на максимальной скорости.

        Args:
            distance: расстояние в км

        Returns:
            Время в пути с учетом реалистичной скорости (80% от максимальной)
        """
        realistic_speed = self.max_speed * 0.8
        return distance / realistic_speed

    def __str__(self) -> str:
        base_str = super().__str__()
        return (f"{base_str} "
                f"Марка: {self.brand}. "
                f"Расход топлива: {self.fuel_consumption} л/100км")

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}("
                f"brand={self.brand!r}, "
                f"fuel_consumption={self.fuel_consumption!r}, "
                f"max_speed={self.max_speed!r}, "
                f"capacity={self.capacity!r})")


if __name__ == "__main__":
    # Пример использования
    bus = TransportVehicle("Автобус", 90.0, 50)
    print(bus)
    print(f"Время пути на 180 км: {bus.calculate_travel_time(180):.2f} ч")

    my_car = Car("Toyota", 8.5, 180.0)
    print("\n" + str(my_car))
    print(f"Время пути на 180 км: {my_car.calculate_travel_time(180):.2f} ч")
    print(f"Стоимость поездки: {my_car.calculate_travel_cost(180, 50):.2f} руб")
    print(repr(my_car))