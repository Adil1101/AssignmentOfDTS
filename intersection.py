def intersection(l1,l2):
    return list(set(l1) & set(l2))
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
print(intersection(l1,l2))
