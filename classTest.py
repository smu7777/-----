class Car:
    color = ""
    speed = 0

    def __init__(self, color, speed, person):
        self.color = color
        self.speed = speed
        self.person = person

    def accelerate(self, increment):
        self.speed += increment
        print(f"The car accelerates by {increment} km/h. New speed: {self.speed} km/h")
    def brake(self, decrement):
        if self.speed - decrement < 0:
            print("Speed cannot be negative. Setting speed to 0.")
            self.speed = 0
        else:
            self.speed -= decrement
        print(f"The car slows down by {decrement} km/h. New speed: {self.speed} km/h")

Car1 = Car("Red", 50, 9)
Car1.accelerate(20)
print(Car1.speed)
print(Car1.person)