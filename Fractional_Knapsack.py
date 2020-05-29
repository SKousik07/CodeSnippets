"""
   input:
      n
      p1 w1
      p2 w2
      .  .
   output:
      total profit
"""

n=int(input("enter n"))
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
w=int(input("enter Capacity"))

l.sort(key= lambda a:a[0]//a[1],reverse=True)#sort based on profit/weight ratio
profit=0
weight=0
i=0
for i in l:
    if weight+i[1] <=w:
        weight=weight+i[1]
        profit+=i[0]
    else:
        rem=w-weight
        profit+= int((rem/i[1])*i[0])
        break
print(profit)
    
    
