inFp=None 
inList,inStr=[], ""

inFp=open("/Users/kimhyeonjung/Library/Mobile Documents/com~apple~TextEdit/Documents/data1.txt","r") # open()함수는 파일을 열고, 파일 객체를 반환함.
# "r"은 읽기 모드로 파일을 열겠다는 의미임.

inList=inFp.readlines()  ## readline"s"()는 파일의 모든 줄을 읽어 리스트로 반환함.
for inStr in inList:
    print(inStr, end="")

inFp.close()