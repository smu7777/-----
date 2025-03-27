a=int(input("입력 진수 결정(16/10/8/2) :"))
b=input("값 입력:")

if a==16:
    print("16진수 ==>",b)
    print("10진수 ==>",int(b,16))
    print("8진수 ==>",oct(int(b,16)))
    print("2진수 ==>",bin(int(b,16)))
if a==10:
    print("16진수 ==>",hex(int(b)))
    print("10진수 ==>",b)
    print("8진수 ==>",oct(int(b)))
    print("2진수 ==>",bin(int(b)))
if a==8:
    print("16진수 ==>",hex(int(b,8)))
    print("10진수 ==>",int(b,8))
    print("8진수 ==>",b)
    print("2진수 ==>",bin(int(b,8)))
if a==2:
    print("16진수 ==>",hex(int(b,2)))
    print("10진수 ==>",int(b,2))
    print("8진수 ==>",oct(int(b,2)))
    print("2진수 ==>",b)