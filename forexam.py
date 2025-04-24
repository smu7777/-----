result,R="",0



while True:
    while True:
        try:
            A=int(input("1.입력한 수식 계산 2. 두 수 사이의 합계"))
            break
        except ValueError:
            print("정수를 입력해주세요")
    if A==1:
        B=input("계산할 수식을 입력해주세요")
        result=eval(B)
        break
    elif A==2:
        while True:
            try:
                B=int(input("첫번째 숫자를 입력해주세요"))
                C=int(input("두번째 숫자를 입력해주세요"))   #B<C 가정
                break
            except ValueError:
                print("다시 입력해주셈")
        for i in range(B,C+1):
            R=R+i
        result=R
        break
    else:
        print("1,2중에 입력해주세요")

print(result)