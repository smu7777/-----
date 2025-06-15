import os

outFp = None
outStr = ""
fileName = input("작성할 파일의 경로를 입력해주세요:")

if os.path.exists(fileName):
    outFp = open(fileName, "w")
    while True:
        outStr = input("내용 입력:")
        if outStr != "":
            outFp.writelines(outStr + "\n")
        else:
            break
else:
    print("파일이 없습니다")

outFp.close()
print("정상적으로 파일에 씀")
    