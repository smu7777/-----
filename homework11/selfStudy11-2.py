inFp = None
inList, inStr = [], ""

inFp = open("hello.txt", "r")

inList = inFp.readlines()
for inStr in inList:
    print("%d: %s"%(inList.index(inStr)+1, inStr), end = "")

inFp.close()