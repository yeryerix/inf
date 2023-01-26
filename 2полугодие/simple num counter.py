a=[]
for i in range (2,1000):
    if all (i%x!=0 for x in range (2,i-1)):
        a.append(i)

for n in range (1,100):
    b=117+4*n
    if b==a:
        print (n)