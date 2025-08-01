
class Animal:
    def eat(self):
        print("eat")
    def __init__(self):
        self.age = 1


class Mammal(Animal):
    def walk(self):
        print("walk")
        
class Fish(Animal):
    def swim(self):
        print("swim")
        
e=Mammal()

e.eat()
print(e.age)
    
    