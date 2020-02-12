class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def move(self):
        print("Move")


    def draw(self):
        print("Draw")


Point1 = Point(x=10,y=20)
Point1.draw()
Point1.move()
print(f"x={Point1.x}")
print(f'y={Point1.y}')


class Person:
    def __init__(self,name):
        self.name = name
        print("In Init with name "+name)


    def talk(self):
        print(f"Hi, I am {self.name}")


p=Person("Sandeep")
p.talk()
p1=Person("John Smith")
p1.talk()
