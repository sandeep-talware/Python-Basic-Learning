class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def be_annoying(self):
        print('be_annoying')


d = Dog()
d.walk()
d.bark()
c = Cat()
c.walk()
c.be_annoying()
m=Mammal()
m.walk()