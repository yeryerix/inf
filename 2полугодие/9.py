# загрузка текста из txt
text=t.split(";")
#result = [int(item) for item in text]
result = list(map(int, text))
x=0
y=x+6
counter=double_num=0

while True:
   n=0
   res6=result[x:y]
   for element in res6:
      if res6.count(element)>2:
         for yy in range(res6.count(element)): res6.remove(element) 
         # удаление значений больше 2 штук
      if res6.count(element)==2:
         n+=2   
         double_num=element 
         res6.remove(element)
         res6.remove(element)

   if n==2 and len(res6)==4:  
      if (sum(res6)/len(res6))<=(double_num*2): counter+=1

   print(counter)
   if y>=len(result):break         
   x=x+6
   y=x+6
