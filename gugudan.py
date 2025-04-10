a,b,g=0,0,""

for a in range(2, 10):
    g=g+("#   %d단   #" % a)
print(g)

for a in range(1, 10):
    g=""
    for b in range(2, 10):
        g=g+str("%2dX %2d= %2d " % (b,a,b*a))
    print(g)