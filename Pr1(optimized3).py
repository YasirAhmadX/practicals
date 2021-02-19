s=input()
d={}
for i in s:
    if i not in d:
        d[i]=s.count(i)
print('Number of characters in the string: ',len(s))
print('Frequency of each characters: ',d)
#most optamizied code has been named pr1.py