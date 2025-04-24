#로또 추첨하기

import random

def getNumber():
    return random.randrange(1,46)

lotto=[]
num=0

print("로또 추첨 시작")
 
while True:
    num=getNumber()

    if lotto.count(str(num)) == 0:
        lotto.append(str(num))

    if len(lotto)>=6:
        print("추첨끝")
        break

lotto.sort()
print("추첨된 로또 번호",end="")
for i in range(6):
    print(f"{lotto[i]} ",end="")


#값에 의한 전달, 참조에 의한 전달
def func(p):
    p[0]=222

v=(111,436)
func(v)
print(v[0])