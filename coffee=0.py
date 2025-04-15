coffee=0
import time

def coffee_machine(button):
    print()
    print("#1. (자동으로) 뜨거운 물을 준비한다.");
    time.sleep(1)
    print("#2. (자동으로) 종이컵을 준비한다.");
    time.sleep(1)

    if button==1:
        print("#3.(자동으로) 보통커피를 탄다.")
    elif button==2:
        print("#3.(자동으로) 설탕커피를 탄다.")
    elif button==3:
        print("#3.(자동으로) 블랙커피를 탄다.")
    else:
        print("#3. (자동으로) 아무거나 탄다.\n")
    time.sleep(1)

    print("#4.(자동으로) 물을 붓는다.");
    time.sleep(1)
    print("#5.(자동으로) 스푼으로 젓는다.");
    print()

coffee=int(input("A손님, 어떤 커피 드릴까요?(1:보통, 2:설탕,3:블랙)"))
coffee_machine(coffee)
time.sleep(1)
print("A손님~커피 여기 있습니다.");
time.sleep(1)

coffee=int(input("B손님, 어떤 커피 드릴까요?(1:보통, 2:설탕,3:블랙)"))
coffee_machine(coffee)
print("B손님~커피 여기 있습니다.");

coffee=int(input("어떤 커피 드릴까요?(1:보통, 2:설탕,3:블랙)"))
coffee_machine(coffee)
print("C손님~커피 여기 있습니다.");


