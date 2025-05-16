inFp=None
inStr=""

inFp=open("/Users/kimhyeonjung/Library/Mobile Documents/com~apple~TextEdit/Documents/data1.txt","r")

while True:
    inStr=inFp.readline()
    if inStr=="":
        break
    print(inStr, end="")

inFp.close()