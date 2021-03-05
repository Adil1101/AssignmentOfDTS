def Check(s):
    open_t=tuple('({[')
    closed_t=tuple(')}]')
    m=dict(zip(open_t,closed_t))
    q=[]
    for x in s:
        if x in open_t:
            q.append(m[x])
        elif x in closed_t:
            if not q or x !=q.pop():
                return False
    if not q:
        return True
    else:
        return False
st=input()
print(Check(st))
