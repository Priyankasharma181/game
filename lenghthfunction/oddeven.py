list_1 = [7,8,4,2,3,5]
i=0
even=0
odd=0
a=0
b=[]
while i< len(list_1):
    if list_1[i]%2==0:
        a=list_1[i]
    else:
        b.append(list_1[i])
        c=sorted(b)
    c.append(a)    
    i+=1
# print(a)
print(c)





