import time

def calc(A,B,op):
    if op=="+":
        result=A+B
        return "덧셈",result
    elif op=="-":
        result=A-B
        return "뺄셈",result
    elif op=="*":
        result=A*B
        return "곱셈",result
    else:
        result=A/B
        return "나눗셈",result
    
def clean(x):
    return int(x) if x == int(x) else x
    
while True:
    operator=input("계산하고 싶은 연산을 입력하세요(+,-,*,/).")
    if operator in ["+","-","*","/"]:
        break
    else:
        print("연산 기호를 다시 입력해주세요.")
        time.sleep(0.5)
while True:
    try:
        a=float(input("첫 번째 수를 입력해주세요"))
        break
    except ValueError:
        print("첫 번째 수를 다시 입력해주세요.")
while True:
    try:
        b=float(input("두 번째 수를 입력해주세요"))
        if b==0 and operator=="/":
            print("0으로 나눌 수 없습니다. 두 번째 수를 다시 입력해주세요.")
        else:
            break
    except ValueError:
        print("두 번째 수를 다시 입력해주세요.")

op,res=calc(a,b,operator)
print(f"두 수 간 {op}을 시작합니다")
time.sleep(1)
print(f"##계산결과:{clean(a)}{operator}{clean(b)}={clean(res)}")