"""
Создайте класс Device с атрибутами brand, model и методом turn_on() (выводит "Устройство включено").
Реализуйте подклассы:
Smartphone (добавляет атрибут os, метод turn_on() выводит "Смартфон включен"),
Laptop (добавляет атрибут screen_size, метод turn_on() выводит "Ноутбук включен").
"""

class Device:
    def __init__(self, brand, model):
        self.brand = str(brand)
        self.model = str(model)

    def turn_on(self):
        return "Устройство включено"


class Smarthone(Device):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)
        self.os = str(os)


    def turn_on(self):
        return "Смартфон включен"


class Laptop(Device):
    def __init__(self, brand, model, x, y):
        super().__init__(brand, model)
        self.screen_size = (x, y)

    def turn_on(self):
        return "Ноутбук включен"


phone = Smarthone("ggg", "12e", "yyy")

laptop = Laptop("nnn", "13r", 1, 2)

print(laptop.turn_on())