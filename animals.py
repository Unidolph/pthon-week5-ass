class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

    def make_sound(self):
        pass

class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying through the air! 🦅")

    def make_sound(self):
        print(f"{self.name} says: Tweet! 🎵")

class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming in the water! 🐠")

    def make_sound(self):
        print(f"{self.name} says: Blub blub! 💭")

class Dog(Animal):
    def move(self):
        print(f"{self.name} is running on four legs! 🐕")

    def make_sound(self):
        print(f"{self.name} says: Woof! 🗣️")

# Example usage
if __name__ == "__main__":
    animals = [
        Bird("Polly"),
        Fish("Nemo"),
        Dog("Max")
    ]

    print("Animals demonstrating polymorphism:")
    for animal in animals:
        animal.move()
        animal.make_sound()
        print()