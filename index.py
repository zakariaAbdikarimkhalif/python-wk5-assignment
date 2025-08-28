class Animal:
    def _init_(self, name):
        self.name = name
    
    def move(self):
        return "Some movement"
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def move(self):
        return f"{self.name} runs on four legs"
    
    def speak(self):
        return f"{self.name} says: Woof!"

class Bird(Animal):
    def move(self):
        return f"{self.name} flies in the sky"
    
    def speak(self):
        return f"{self.name} says: Tweet!"

class Fish(Animal):
    def move(self):
        return f"{self.name} swims in water"
    
    def speak(self):
        return f"{self.name} makes bubbles"


animals = [
    Dog("Buddy"),
    Bird("Tweety"), 
    Fish("Goldie")
]

print("Animal Movement Demo:")
print("=" * 20)
for animal in animals:
    print(animal.move())
    print(animal.speak())
    print()

print("Polymorphism Example:")
print("=" * 20)
for animal in animals:
    action = animal.move()
    sound = animal.speak()
    print(f"{animal.name}: {action} and {sound}")