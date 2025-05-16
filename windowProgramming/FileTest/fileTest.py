inFp= None
inStr=""

inFp= open("/Users/kimhyeonjung/Library/Mobile Documents/com~apple~TextEdit/Documents/data1.txt","r")

inStr=inFp.readline()
print(inStr, end="")

inStr=inFp.readline()
print(inStr, end="")

inStr=inFp.readline()
print(inStr, end="")

inFp.close()

