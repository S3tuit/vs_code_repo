from math import sqrt

class Car():

    def __init__(self, hp, weight):
        self.hp = hp
        self.speed = 0
        self.weight = weight

    def accelerate(self, time):
        for i in range(0, time):
            try:
                acc = sqrt(-(self.weight/self.hp)*(i**2) + (self.hp/2)*i + (self.hp))-(self.speed+1)/5.9
            except ValueError:
                acc = 0.3
            round(acc, 2)
            self.speed = self.speed + (acc*i)
            print(self.speed)
    
    def braking(self, time):
        for _ in range(0, time):
            self.speed = self.speed - 4
            print(self.speed)

mustang = Car(1001, 2000)
mustang.accelerate(5)
mustang.braking(3)