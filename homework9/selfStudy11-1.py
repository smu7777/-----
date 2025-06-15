inFp = None
inStr = ""
i = 0

inFp = open("hello.txt", "r")

while True:
    inStr = inFp.readline()
    i = i + 1
    if inStr == "":
        break
    print("%d: %s"%(i,inStr), end='')

inFp.close()