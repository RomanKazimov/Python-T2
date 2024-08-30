from abc import ABC, abstractmethod
from typing import Any

class Animal(ABC):
    __count = 0
    
    def __init__(self, name, gender, breed, color) -> None:
        self._name = name
        self._gender = gender
        self._breed = breed
        self._color = color
        Animal.__count += 1
    
    def get_name(self):
        return self._name
    
    @staticmethod
    def get_count():
        return Animal.__count
    
    def __str__(self):
        return self._name
    
    @abstractmethod
    def display_info(self):
        return self._name, self._gender, self._breed, self._color
    
    def get_voice(self):
        pass
    
    def __setattr__(self, name: str, value: Any) -> None:
        return super().__setattr__(name, value)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("name bosh olmamalidi")
        self._name = value
    
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, value):
        if not value:
            raise ValueError("gender bosh olmamalidi")
        self._gender = value
    
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, value):
        if not value:
            raise ValueError("Cinsini duz vurmadiz")
        self._breed = value
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        if not value:
            raise ValueError("rengini duz vurmadiz")
        self._color = value

class Cat(Animal):
    def __init__(self, name, gender, breed, color, fluffily):
        super().__init__(name, gender, breed, color)
        self._fluffily = fluffily
    
    @property
    def fluffily(self):
        return self._fluffily
    
    @fluffily.setter
    def fluffily(self, value):
        if not value:
            raise ValueError("Tukluluyu qeyd edmediz")
        self._fluffily = value
            
    def display_info(self):
        return self._name, self._gender, self._breed, self._color, self._fluffily
    
    def get_voice(self):
        return "Myau"
    
    def __setattr__(self, name: str, value: Any) :
        return super().__setattr__(name, value)

class Dog(Animal):
    def __init__(self, name, gender, breed, color, size):
        super().__init__(name, gender, breed, color)
        self._size = size
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if not value:
            raise ValueError("qaqula razmer yoxdu")
        self._size = value
    
    def display_info(self):
        return self._name, self._gender, self._breed, self._color, self._size
    
    def get_voice(self):
        return "Bark Bark"

objects = []
while True:
    a = input("It, Pisiy, 1, 2: ")
    while a != "1" and a != "2":
        a = input("It, Pisiy, 1, 2: ")   
    
    name = input("Heyvanin adi: ")
    gender = input("Heyvanin cinsi: ")
    breed = input("Heyvanin cinsin: ")
    color = input("Heyvanin rengi: ")
    if a == "1":
        fluffily = input("Pishiyin tukluluyu: ")
        try:
            cat = Cat(name, gender, breed, color, fluffily)
            objects.append(cat)
        except ValueError as e:
            print(f"Xeta: {e}")
    elif a == "2":
        size = input("Itin olcusu: ")
        try:
            dog = Dog(name, gender, breed, color, size)
            objects.append(dog)
        except ValueError as e:
            print(f"Xeta: {e}")
    else:
        print("Zehmet olmasa 1 yaxud 2 secin")
        continue

    more = input("Davam etmek (he/yox): ")
    if more.lower() != "he":
        break

for obj in objects:
    print(f"{obj.__class__.__name__}: {obj.display_info()} | Ses: {obj.get_voice()}")

