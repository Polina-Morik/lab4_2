class Car:
    """ Базовый класс. Автомобили """

    def __init__(self, brand: str, color: str, age_car: int, mileage: int):
        self.brand = brand
        self.color = color
        self.age_car = age_car
        self.mileage = mileage

    def __str__(self):
        return f'Автомобиль "{self.brand}", {self.color} цвет'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.brand}, {self.color})'

    def calculate_mileage(self) -> int:
        """ Расчёт пробега автомобиля"""
        return self.age_car * self.mileage

    def cost_car(self) -> int:
        """ Расчёт примерной стоимости автомобиля. Зависит от марки, цвета, возраста и пробега автомобиля"""
        ...

class Motorcar(Car):
    """Дочерний класс. Легковой автомобиль """

    def __init__(self, brand: str, color: str, age_car: int, mileage: int, number_seats: int):
        super().__init__(brand, color, age_car, mileage)
        self.number_seats = number_seats

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.brand}, {self.color}, {self.number_seats})'

    def cost_car(self) -> int:
        """ Расчёт примерной стоимости автомобиля. Зависит от марки, цвета, возраста и пробега автомобиля """
        """ Перегрузка метода. Так как расчет стоимости зависит еще от количества мест в автомобили """
        print(f"Вызван метод класса {self.__class__.__name__}")
        ...


class Cargocar(Car):
    """Дочерний класс. Грузовой автомобиль """

    def __init__(self, brand: str, color: str, age_car: int, mileage: int, tonnage: int):
        super().__init__(brand, color, mileage, age_car)
        self.tonnage = tonnage

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.brand}, {self.color}, {self.tonnage})'

    def cost_car(self) -> int:
        """ Расчёт примерной стоимости автомобиля. Зависит от марки, цвета, возраста и пробега автомобиля """
        """ Перегрузка метода. Так как расчет стоимости зависит еще от грузоподъемности """
        print(f"Вызван метод класса {self.__class__.__name__}")
        ...

if __name__ == "__main__":
    motorcar = Motorcar("КИА", "черный", 10000, 5, 5)
    cargocar = Cargocar("Мазда", "белый", 15000, 3, 200)


    print(motorcar)
    print(motorcar.calculate_mileage())
    print(motorcar.cost_car())

    print(cargocar)
    print(cargocar.calculate_mileage())
    print(cargocar.cost_car())

    pass
