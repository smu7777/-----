a=float(input("1. 입력한 수식 계산 2. 두 수(정수)의 합계:"))

if a==1:
    b=input("*** 수식을 입력하세요:")
    print(b,"결과는",eval(b),"입니다.")
elif a==2:
    c=int(input("*** 첫 번째 숫자를 입력하세요:"))
    d=int(input("*** 두 번째 숫자를 입력하세요:"))
    if c>d:
        print(d,"+...+",c,"는",sum(range(d,c+1)),"입니다.")
    elif d>c:
        print(c,"+...+",d,"는",sum(range(c,d+1)),"입니다.")
    else:
        print("오류입니다. 두 수를 다르게 입력해주세요")
else:
    print("지금 뭐하시는 거죠? 1 또는 2를 입력해주세요.")
