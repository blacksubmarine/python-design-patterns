from abc import ABC, abstractmethod

# Animal Interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Animals
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Tweet!"

# Animal Factory
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        elif animal_type == 'bird':
            return Bird()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Client code
if __name__ == "__main__":
    # List of animal types to create
    animal_types = ['dog', 'cat', 'bird']

    # Create and use animals
    for animal_type in animal_types:
        animal = AnimalFactory.create_animal(animal_type)
        print(f"A {animal_type} says: {animal.speak()}")
