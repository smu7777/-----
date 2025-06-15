class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        if (self.speed+value) <= 150:
            self.speed += value
        else:
            print("최고 속도는 150km 입니다.")
            self.speed = 150

    def downSpeed(self, value):
        self.speed -= value

myCar1= Car()
myCar1.color = "빨강"
myCar1.speed = 80

myCar2= Car()
myCar2.color = "파랑"
myCar2.speed = 160

myCar3= Car()
myCar3.color = "노랑"
myCar3.speed = 0

myCar1.upSpeed(80)
print("자동차1의 색상은 %s 이고, 현재 속도는 %d km 입니다." % (myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색상은 %s 이고, 현재 속도는 %d km 입니다." % (myCar2.color, myCar2.speed))

myCar3.upSpeed(0)
print("자동차3의 색상은 %s 이고, 현재 속도는 %d km 입니다." % (myCar3.color, myCar3.speed))