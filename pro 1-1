b=int(input())
x=[]
for i in range(b):
  a=input()
  x.append(a)
mv=min(x,key=len)
x.remove(mv)
for i in range(len(mv)):
  for j in range(len(x)):
     cv=x[j]
     if mv[:i+1]==cv[:i+1]:
       result=mv[:i+1]
     else:
       break
print(result)
