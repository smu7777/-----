inFp,outFp= None, None
inStr, outStr="", ""
i=0
secu=0

secuYN= input("1.암호화 2. 암호해석중 선택:")
inFname= input("읽을 파일 이름을 입력하시오: ")
outFname= input("쓸 파일 이름을 입력하시오: ")

if secuYN == "1":
    secu=100
elif secuYN == "2":
    secu=-100

inFp= open(inFname, "r", encoding="utf-8")
outFp= open(outFname, "w", encoding="utf-8")

while True:
    inStr= inFp.readline()
    if not inStr:
        break

    outStr=""
    for i in range(0, len(inStr)):
        ch= inStr[i]
        chNum= ord(ch)
        chNum = chNum + secu
        ch2= chr(chNum)
        outStr= outStr + ch2

    outFp.write(outStr)

inFp.close()
outFp.close()
print(f"{outFname} --> {inFname} 변환완료")
