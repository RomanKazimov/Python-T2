from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, seat, price, color, freshnes):
        self.seat = seat
        self.price = price
        self.color = color
        self.freshnes = freshnes

    @abstractmethod
    def get_info(self):
        return self.seat, self.price, self.color, self.freshnes
    
class Bus(Vehicle):
    def __init__(self, seat, price, color, freshnes, door, wheel):
        super().__init__(seat, price, color, freshnes)
        self.door = door
        self.wheel = wheel  
    def get_info(self):
        return self.seat, self.price, self.color, self.freshnes, self.door, self.wheel

class Car(Vehicle):
    def __init__(self, seat, price, color, freshnes, door, wheel):
        super().__init__(seat, price, color, freshnes)
        self.door = door
        self.wheel = wheel
    def get_info(self):
        return self.seat, self.price, self.color, self.freshnes, self.door, self.wheel
    

class Ship(Vehicle):
    def __init__(self, seat, price, color, freshnes, door):
        super().__init__(seat, price, color, freshnes)
        self.door = door
    def get_info(self):
        return self.seat, self.price, self.color, self.freshnes, self.door

class Bicycle(Vehicle):
    def __init__(self, seat, price, color, freshnes, wheel):
        super().__init__(seat, price, color, freshnes)
        self.wheel = wheel
    def get_info(self):
        return self.seat, self.price, self.color, self.freshnes, self.wheel

class Plane(Vehicle):
    def __init__(self, seat, price, color, freshnes, door, wing):
        super().__init__(seat, price, color, freshnes)
        self.door = door
        self.wing = wing
    def get_info(self):
        return self.seat, self.price, self.color, self.freshnes, self.door, self.wing
    

obj = Plane(100, 100000, "White", True, 2, 2)
print(obj.get_info())


