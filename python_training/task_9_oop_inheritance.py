class Mammal:
    className : str = "mammal"

class Dog(Mammal):
    species : str = "dog"

dog = Dog()
print(dog.species)
print(dog.className)