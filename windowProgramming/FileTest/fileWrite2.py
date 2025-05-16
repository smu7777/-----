inFp, outFp=None, None
inStr=""

inFp=open("/Applications/무제 폴더/windowProgramming/FileTest/data1.txt","r")
outFp=open("/Applications/무제 폴더/windowProgramming/normal.txt","w")

inList=inFp.readlines()
for inStr in inList:
    outFp.write(inStr)

inFp.close()
outFp.close()
print("----파일이 정상적으로 복사되었습니다.----")
