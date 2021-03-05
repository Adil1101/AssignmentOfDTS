def singleOne(n):
    return 2*sum(set(n))-sum(n)
n=list(map(int,input().split()))
print(int(singleOne(n)))
