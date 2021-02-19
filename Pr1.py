'''<yasir_ahmad>
WAP to count the number of characters in a string and generate a dictionary where the key values are all the unique characters from
the string and its associated values refer its frequency.
'''

s=input()
d={}
for i in s:
    d[i]=0
for i in s:
    d[i]+=1
print('Number of characters in the string: ',len(s))
print('Frequency of each characters: ',d)