a,b = map(int,input().split(" "))
print([pow(a,i) for i in range(1,b+1) if i != 2 and i != b-1])