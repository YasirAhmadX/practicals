s=list(input())
d={}
itr=0
for i in range(len(s)):
    if s[i] not in d:
        d[s[i]]=0
        for j in range(i,len(s)):
            if s[j]==s[i]:
                d[s[i]]+=1
            itr+=1
    itr+=1
print(d)
print(f'iteration= {itr};n={len(s)};n2={len(s)**2}')
