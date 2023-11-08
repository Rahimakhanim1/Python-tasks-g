class Car():
    def __init__(self,color,name):
        self.color = color
        self.name = name

class childCar(Car):
    def __init__(self,color,name,number):
        super().__init__(color,name)
        self.number = number

first = Car("red","chevrolet")
second= childCar(1)
print(first.number)