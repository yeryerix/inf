spisok=[]
for num in range(2,1000):
  n=0
  for delit in range (2,100):
    if num%delit==0: n+=1
  
  if n==0:spisok.append(num)
        
flag=False
for i in spisok:
    for y in range (100):
        if y*4+117==i and flag==False:
            print(y, i)
            flag=True
