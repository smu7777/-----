contents = ""
txt = open("hello.txt", "r")
for contents in txt.readlines():
    print(contents.strip())
txt.close()