# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, о
# становилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar
# и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    # задаем атрибуты класса
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    #  задаем метод
    def on_route(self):
        return f'{self.name} is on route'

    def stop(self):
        return f'{self.name} is stopped'

    def right_turn(self):
        return f'{self.name} is make a right turn'

    def left_turn(self):
        return f'{self.name} is make a left turn'

    def show_speed(self):
        return f'Speed {self.name} is {self.speed} '


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'TownCar speed {self.name} is {self.speed}')

        if self.speed < 60:
            return f'{self.name} speeding'
        else:
            return f'{self.name} speed not exceeded'


class SpotrCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'WorkCar speed {self.name} is {self.speed}')

        if self.speed > 40:
            return f'{self.name} speeding'
        else:
            return f'{self.name} speed not exceeded'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def LAPD(self):
        if self.is_police:
            return f'{self.name} LAPD unit'
        else:
            return f'{self.name} civilian vehicle'


Porsche = SpotrCar(200, 'yellow', 'Porsche', False)
Toyota = TownCar(43, 'white', 'Toyota', False)
Freightliner = WorkCar(65, 'red', 'Freightliner', False)
Dodge = PoliceCar(110, 'Black and White', 'Dodge', True)

print(Freightliner.left_turn())
print(f'{Porsche.right_turn()}, then {Toyota.stop()}')
print(f'{Dodge.name} is {Dodge.color}')
print(Porsche.show_speed())
print(Toyota.show_speed())
print(Freightliner.show_speed())
print(f'Dodge a police vehicle?', Dodge.is_police)