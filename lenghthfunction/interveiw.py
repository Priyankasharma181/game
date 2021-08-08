list_1=[6,4,5,12,8]
i=0
while i< len(list_1):
    j=0
    while j<len(list_1)-1:
        if list_1[j+1]<list_1[j]:
            list_1[j],list_1[j+1] = list_1[j+1],list_1[j]
        j+=1
    i+=1
print(list_1) 
x=[]
for j in range(list_1[0],list_1[-1]+1):
    if j not in list_1:
        x.append(j)
print(len(x))
print(x)

    
        

