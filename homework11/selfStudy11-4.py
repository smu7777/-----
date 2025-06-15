inFp, outFp = None, None
inStr = ""
sourceFile = ""
targetFile = ""

sourceFile = input("소스 파일의 경로를 입력하세요:")
targetFile = input("타깃 파일의 경로를 입력하세요:")
inFp = open(sourceFile, "r")
outFp = open(targetFile, "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("%s 파일이 %s 파일로 복사되었음"%(sourceFile, targetFile))