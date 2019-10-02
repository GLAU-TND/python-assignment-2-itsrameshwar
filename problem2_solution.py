l=eval(input())
k=int(input())
for i in range(len(l)):
    for j in range(i,len(l)):
        if sum(l[i:j+1])==k:
            print(l[i:j+1])
