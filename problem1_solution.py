s=input()
k=int(input())
l1=s.split()
l2=[]
s1=''
for i in l1:
    if len(s1+i)<=k:
        s1=s1+i+' '
    else:
        s1.strip()
        l2.append(s1)
        s1=i+' '
print(l2)


