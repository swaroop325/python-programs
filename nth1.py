n,a=input().split()
x=int(n)
y=int(a)
c=[]
sum=0
for i in range(x):
    c.append(int(input()))
for i in range(y):
    sum+=c[i]



print(sum)   
    
