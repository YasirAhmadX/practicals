
s=input()
d={}
c=0
for i in s:
    d[i]=0
    c+=1
for i in d.keys():
    d[i]=s.count(i)
    c+=1
print(f'd={d} and c={c}')
