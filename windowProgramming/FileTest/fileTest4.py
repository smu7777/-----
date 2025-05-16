import os

inFp=None
fName, inList, inStr="", [], ""

fName=input("읽을 파일 이름을 입력하시오: ")

if os.path.exists(fName):
    inFp=open(fName, "r")
    inList=inFp.readlines()
    for inStr in inList:
        print(inStr, end="")
    inFp.close()

else:
    print("파일이 없습니다.")