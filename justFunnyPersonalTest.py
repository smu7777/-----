hap,plusList,length,i,finish=0,[],0,0,False
import time

def para_func(*para):
    result=0
    for num in para:
        result=result+num
    return result

while True:
    try:
        length=int(input("더하기 싶은 수의 개수를 입력해주세요."))
        break
    except ValueError:
        print("다시 입력해주세요")
        time.sleep(0.7)

while True:
    try:
        while i<length:
            reply=0
            reply=int(input(f"{i+1}번째 숫자를 입력해주세요"))
            plusList.append(reply)
            i+=1
        break
    except ValueError:
        print(f"잘못된 응답입니다. {i+1} 번째부터 다시 입력하시겠습니까?")
        time.sleep(0.5)
        while True:
            earlyFinish=input("나가시려면 \"종료\"를, 계속하시려면 \"계속\"을 입력해주세요.")
            if earlyFinish=="종료":
                finish=True
                break
            elif earlyFinish=="계속":
                break
            else:
                time.sleep(0.4)
                print("잘못된 형식입니다. 다시 입력해주세요.")
        time.sleep(0.5)
    if finish:
        break

if finish:
    print("프로그램을 종료합니다.")
else:
    print(f"입력하신 {i}개 수를 다 더하면 {para_func(*plusList)}입니다")