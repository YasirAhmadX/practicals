## Practical 1

> Write a program to count the number of characters in a string and generate a dictionary where the key values are all the unique characters from
the string and its associated values refer its frequency.

```python
s=input()
d={}
for i in s:
    d[i]=0
for i in s:
    d[i]+=1
print('Number of characters in the string: ',len(s))
print('Frequency of each characters: ',d)
```

## Practical 2

> WAP to create a list with 'n' number of items where each item refers a tuple which consist of the data as given below:
list=[('aman',45,52,62,52,63),('rahul',52,21,20,25,56),.......(stud_name,mark1,mark2,mark3,mark4,mark5)]
>
>Find the details of those students who is securing more than 65% as their average and display the total count of such students.
```python
l=[]
for i in range(int(input('Enter no. of students: '))):
    t=[input('Enter student\'s name: ')]
    print('Enter marks: ')
    for i in range(5):
        t.append(int(input('>')))
    l.append(tuple(t))
print('< Students who scored more than 65% >')
c=0
for t in l:
    avg=(t[1]+t[2]+t[3]+t[4]+t[5])/5
    if avg>65:
        print('Stduent\'s name:',t[0])
        print('Marks:',t[1],t[2],t[3],t[4],t[5])
        print('Average:',avg,'%')
        c+=1
print('Number of stduents to get more than 65%:',c)
```

## Practical 3

>WAP to enter 'n' no. of students's information in the form of list of tuple where each tuple consists of roll no. and its corresponding
name.Eg:-[(1,'adya'),(2,'abhinav'),.......(roll,'name')]. Write a menu driven choice for the keys 1 and 2, where 1 is used to sequential search and 2 for binary search.
>
>Ask a roll number from the user and search the desired information accordingly.

```python
def LinearSearch(s):
    for i in l:
        if i[0]==s:
            return 'Desired record:'+str(i)
    return 'No matching record found!'
def BinarySearch(L,s):
    L.sort()
    ub=len(L)-1
    lb=0
    check=0

    while check==0 and lb<=ub:
        if s==L[(lb+ub)//2][0]:
            return 'Desired record:'+str(L[(lb+ub)//2])
        else:
            if s<L[(lb+ub)//2][0]:
                ub=(ub+lb)//2 -1
            else:
                lb=(lb+ub)//2 +1
    return 'No matching record found!'


l=[]
for i in range(int(input('Enter number of students: '))):
    t=(int(input('Enter roll of the student: ')),input('Enter name of the student: '))
    l.append(t)



while True:
    s=int(input('Enter roll to be searched: '))
    n=(input('Enter: \n1 for Linear Search\n2 for Binary Search\n:'))
    if n=='1':
        print(LinearSearch(s))
    elif n=='2':
        print(BinarySearch(l,s))
    else:
        print('Invalid choice!')
        break
```
