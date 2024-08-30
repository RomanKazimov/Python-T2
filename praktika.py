class Country:
    __country_count = 0
    def __init__(self, name, capital, population, continent):
        self.name = name
        self.capital = capital
        self.population = population 
        self.continent = continent
        Country.__country_count += 1
    def parametrs(self):
        return self.name, self.capital, self.capital, self.population, self.continent
    def __eq__(self, other):
        if other.name == self.name:
            return True
        return False
    @staticmethod
    def getCount():
        return Country.__country_count
    def __str__(self):
        return self.name
    


obj1 = Country("France", "Paris", 10000000, "Europa")
obj2 = Country("France", "Paris", 10000000, "Europa")

print(obj1)
print(obj1 == obj2)
print(Country.getCount())
print(obj1.parametrs())