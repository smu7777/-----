inFp, outFp=None, None
inStr=""

inFp=open("읽을 파일","r")
outFp=open("쓸 파일","w")

inList=inFp.readlines()
for inStr in inList:
    outFp.write(inStr)

inFp.close()
outFp.close()
print("----파일이 정상적으로 복사되었습니다.----")
