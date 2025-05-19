class Car:

    def __init__(self, color = None, car_type = None, year = None):
        self.color = color
        self.car_type = car_type
        self.year = year

    @staticmethod
    def start():
        print('Автомобиль заведен')

    @staticmethod
    def stop():
        print('Автомобиль заглушен')

    def set_year(self, year):
        self.year = year

    def set_car_type(self, car_type):
        self.car_type = car_type

    def set_color(self, color):
        self.color = color
