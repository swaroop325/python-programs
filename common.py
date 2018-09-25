def common_prefix(a,b):
    i = 0
    for i, (x, y) in enumerate(zip(a,b)):
        if x!=y: break
    return a[:i]
a=input()  
b=input()
c=common_prefix(a,b)
print (c)
