import doctest
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand: str, model: str, year: int):
        """
        Создание объекта "Транспортное средство".

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.

        Примеры:
        >>> vehicle = Vehicle("Toyota", "Corolla", 2020)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(year, int):
            raise TypeError("Год должен быть целым числом")
        if year < 1886:  # Первый автомобиль был создан в 1886 году
            raise ValueError("Год должен быть не менее 1886")

        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> None:
        """
        Запуск двигателя транспортного средства.
        """
        ...

    @abstractmethod
    def stop_engine(self) -> None:
        """
        Остановка двигателя транспортного средства.
        """
        ...


class Computer(ABC):
    def __init__(self, cpu: str, ram: int, storage: int):
        """
        Создание объекта "Компьютер".

        :param cpu: Модель процессора.
        :param ram: Объем ОЗУ в гигабайтах.
        :param storage: Объем хранилища в гигабайтах.

        Примеры:
        >>> computer = Computer("Intel i7", 16, 512)
        """
        if not isinstance(cpu, str):
            raise TypeError("Модель процессора должна быть строкой")
        if not isinstance(ram, int) or ram <= 0:
            raise ValueError("Объем ОЗУ должен быть положительным целым числом")
        if not isinstance(storage, int) or storage < 0:
            raise ValueError("Объем хранилища не может быть отрицательным числом")

        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    @abstractmethod
    def power_on(self) -> None:
        """
        Включение компьютера.
        """
        ...

    @abstractmethod
    def power_off(self) -> None:
        """
        Выключение компьютера.
        """
        ...


class Smartphone(ABC):
    def __init__(self, brand: str, model: str, battery_capacity: int):
        """
        Создание объекта "Смартфон".

        :param brand: Марка смартфона.
        :param model: Модель смартфона.
        :param battery_capacity: Вместимость аккумулятора в мАч.

        Примеры:
        >>> smartphone = Smartphone("Apple", "iPhone 14", 3095)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(battery_capacity, int) or battery_capacity <= 0:
            raise ValueError("Вместимость аккумулятора должна быть положительным целым числом")

        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity

    @abstractmethod
    def make_call(self, number: str) -> None:
        """
        Произвести звонок на заданный номер.

        :param number: Номер телефона для звонка.
        """
        ...

    @abstractmethod
    def send_message(self, number: str, message: str) -> None:
        """
        Отправка сообщения на заданный номер.

        :param number: Номер телефона для отправки сообщения.
        :param message: Текст сообщения.
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

