# CS Practicals

This collection of cs practicals questions were collected from [**DAV Public School, Hehal,Ranchi**](http://davhehal.org) and Solutions are written in  _python 3_ .These Practicals cover various topics related to lists , tuples , dictionary , functions , searching algorithms , sorting algorithms , file I/O ,etc. 

---
## INDEX

| Serial Number | Name of practical | Date of practical | Date of submission |
|:-------------:|:------------------:|:------:|:------:|
| 1. | Practical 1 | 14/08/2020  |  |
| 2. | Practical 2 | 18/08/2020  |  |
| 3. | Practical 3 | 22/08/2020  |  |
| 4. | Practical 4 | 28/08/2020  |  |
| 5. | Practical 5 | 24/09/2020  |  |
| 6. | Practical 6 | 12/10/2020  |  |
| 7. | Practical 7 | 26/10/2020  |  |
| 8. | Practical 8 | 4/11/2020   |  |
| 9. | Practical 9 | 6/11/2020   |  |
| 10. | Practical 10 | 6/11/2020  |  |
| 11. | Practical 11 | 10/11/2020 |  |
| 12. | Practical 12 | 13/11/2020 |  |
| 13. | Practical 13 | 23/11/2020 |  |
| 14. | Practical 14 | 24/11/2020 |  |
| 15. | Practical 15 | 27/11/2020 |  |


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
---

## Practical 2

> Write a program to create a list with **n** number of items where each item refers a tuple which consist of the data as given below:
`list=[('aman',45,52,62,52,63),('rahul',52,21,20,25,56),.......(stud_name,mark1,mark2,mark3,mark4,mark5)]`
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

---

## Practical 3

>Write a program to enter **n** no. of students's information in the form of list of tuple where each tuple consists of roll no. and its correspondingname.Example:`[(1,'adya'),(2,'abhinav'),.......(roll,'name')]`. Write a menu driven choice for the keys 1 and 2, where 1 is used to sequential search and 2 for binary search.
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

---

## Practical 4


>Write a program to enter **n** no. of students's information in the form of list of tuple where each tuple consists of roll no. and its corresponding name. Example:`[(1,'adya'),(2,'abhinav'),.......(roll,'name')]`
>
>Sort the records in ascending order by using bubble sort with respect to their corresponding roll nummbers.

```python
def BubbleSort(l):
    for k in range(len(l)-1):
        for j in range(0,len(l)-1-k):
            if l[j][0]>l[j+1][0]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

l=[]
for i in range(int(input('Enter number of students: '))):
    t=(int(input('Enter roll of the student: ')),input('Enter name of the student: '))
    l.append(t)

print('Original List: ',l)
print('Sorted List:' ,BubbleSort(l))
```

---

## Practical 5

>Write a program to input **n** numbers of integer in  a list and print the maximum even numberr present in it , if no even number is present, then
print **'No even numbers is present !'** 

```python
l=[]
for i in range(int(input('Enter no. of entries: '))):
    l.append(int(input()))

evn_number=-1 #-1 is default value, will channge once an even number is found.
for i in l:
    if i%2==0 and i>evn_number:
        evn_number=i

print('No even number is present.' if evn_number==-1 else evn_number)
```

---

## Practical 6

>Write a program to enter **n** number of registered user details in the form of dictionary, where the dictionary contain the following details `{'userid':'password'}`.
Ask the user to search any userid, if it is not present in the dictionary then print **'userid not registered'**, other wise check the corresponding,
password after asking the same from the user and print **'logged successfully'** if the user enters the correct password otherwise print 
**'incorrect password'**.

```python3
d={}
for i in range(int(input('Enter number of entries: '))):
    key=input('Enter userid: ')
    d[key]=input('Enter password: ')

s_userid=input('Enter userid to search: ')
s_passwd=input('Enter password: ')
if s_userid in d:
    if s_passwd == d[s_userid]:
        print('logged successfully.')
    else:
        print('incorrect password.')
else:
    print('userid not registered')
```

---

## Practical 7

>Write a program to input a list having **n** number of elements and print the sum of all prime numbers and all odd numbers.

```python3
l=[]
for i in range(int(input('Enter no. of elements in the list: '))):
    l.append(int(input('Enter element: ')))
sum_odd=sum_prime=0
for i in l:
    j=0
    prime=True
    
    for d in range(2,i//2 +1):
        if i%d==0 or i==1:
            prime=False
    if prime:
        sum_prime+=i

    if i%2!=0:
        sum_odd+=i
    
print('sum of odd no. is: ',sum_odd)
print('sum of prime no. is: ',sum_prime)
```

---

## Practical 8

>Write a program to create a function which takes 3 arguments (say a,b,ch) where a is length b is breadth and ch  is choice whether to compute area or perimeter.
>
>**Note**:- Use positional arguments:
>
>ch==1 for area 
>
>ch==2 for perimeter 
>

```python3
def Area_Perimeter(a,b,ch):
    """
        a(int): Length of the rectangle
        b(int): Breadth of the rectangle
        ch(int): choice
                ch==1>>Area
                ch==2>>Perimeter
        Returns area or perimeter of the rectangle.
    """
    if ch==1:
        return 'Area is '+str(a*b)
    elif ch==2:
        return 'Perimeter is '+str(2*(a+b))
    else:
        return 'Invalid choice.'
a,b,ch=int(input('a: ')),int(input('b: ')),int(input('choice: '))
print(Area_Perimeter(a,b,ch))
#help(Area_Perimeter)
```

---

## Practical 9

>Write a program to create a function which takes 3 arguments (say a,b,ch) where a is length b is breadth and ch  is choice whether to compute area or perimeter.
>
>**Note**:- Use keyword arguments: 
>
>    ch==1 for area 
>    
>   ch==2 for perimeter 
>
   
```python3
def Area_Perimeter(a,b,ch):
    """
        a(int): Length of the rectangle
        b(int): Breadth of the rectangle
        ch(int): choice
                ch==1>>Area
                ch==2>>Perimeter
        Returns area or perimeter of the rectangle.
    """
    if ch==1:
        return 'Area is '+str(a*b)
    elif ch==2:
        return 'Perimeter is '+str(2*(a+b))
    else:
        return 'Invalid choice.'
x,y,choice=int(input('a: ')),int(input('b: ')),int(input('choice: '))
print(Area_Perimeter(a=x,ch=choice,b=y))
#help(Area_Perimeter)
```

---

## Practical 10

>WAP to create a function which takes 3 arguments (say a,b,ch) where a is length ;b is breadth and ch  is choice whether to compute area or perimeter.
>**Note**:- By default it should find area.
>

```python3
def Area_Perimeter(a,b,ch=1):
    """
        a(int): Length of the rectangle
        b(int): Breadth of the rectangle
        ch(int): choice
                ch==1>>Area
                ch==2>>Perimeter
        Returns area or perimeter of the rectangle.
    """
    if ch==1:
        return 'Area is '+str(a*b)
    elif ch==2:
        return 'Perimeter is '+str(2*(a+b))
    else:
        return 'Invalid choice.'
x,y,choice=int(input('a: ')),int(input('b: ')),int(input('choice: '))
print(Area_Perimeter(a=x,ch=choice,b=y))
#help(Area_Perimeter)
```

---

## Practical 11

>Create a module named as **shape.py** which consists of three functions named as `arear(),areas() and areac()` for finding area of rectangle,square and circles resectively.
>Call all these function from another file named as **check.py** using accession operator. 
>

Code for **shape.py**
```python3
def arear(length,breadth):
    '''
        Return area of a rectangle of given length and breadth
    '''
    return length*breadth

def areas(side):
    '''
        Return area of a square of given side
    '''
    return side**2

def areac(radius):
    '''
        Return area of a circle of given radius
    '''
    from math import pi
    return pi*radius**2
```

Code for **check.py**
```python3
import shape
print(shape.areac(15))
print(shape.arear(10,20))
print(shape.areas(4))

```

---

## Practical 12

>Create a module named as **shape.py** which consists of three functions named as `arear(),areas() and areac()` for finding area of rectangle,square and circles resectively.
>Call all these function from another file named as **check2.py** without using accession operator. 
>

Code for **shape.py**
```python3
def arear(length,breadth):
    '''
        Return area of a rectangle of given length and breadth
    '''
    return length*breadth

def areas(side):
    '''
        Return area of a square of given side
    '''
    return side**2

def areac(radius):
    '''
        Return area of a circle of given radius
    '''
    from math import pi
    return pi*radius**2
```

Code for **check2.py**
```python3
from shape import *
print(areac(15))
print(arear(10,20))
print(areas(4))

```

---

## Practical 13

>Write a program to read a text file **student.txt** and count: 
>
>i)how many words are there that start with a vowel 
>
>ii)how many line start with T
>
>iii)number of digits


Get **student.txt** from [here](student.txt)
```python3
f=open('student.txt','r')
c_vowel=c_Tline=c_digits=0

for line in f.readlines():
    if line[0]=='T':
        c_Tline+=1
    for word in line.split():
        if word[0].lower() in ['a','e','i','o','u']:
            c_vowel+=1
        elif word.isdigit():
            c_digits+=1
f.close()
print('Number of lines that start with "T":',c_Tline)
print('Number of words tha start with a vowel:',c_vowel)
print('Number digits:',c_digits)
```

---

## Practical 14

>Write a program to create a file named as **student.txt** which will contain names of **n** number of students.Then create another file **copy.py** in which copyonly those names from **student.txt** which starts with letter **'A'**.
>

Get sample of **student.txt** from [here](student.txt)  
Get sample of **copy.txt** from [here](copy.txt)

```python3
f=open('student.txt','w+')
for i in range(int(input('Enter number of students: '))):
    f.write(input('Enter name: ')+str('\n'))
f.seek(0,0)

c=open('copy.txt','w')
for i in f.readlines():
    if i[0]=='A':
        c.write(i)

c.close()
f.close()
```

---

## Practical 15

>Write a program to enter the details of **n** number of students having their roll,age,name in the form of a nested list`l=[[roll1,age,'name1'],[roll2,age2,'name2']...]`, dump the entire dataset
>in a file **students.txt**,then display back only those records from that file whose age is **more than 16 years**.
>

```python3
from pickle import dump,load
f=open('students.txt','w+b')
list=[]
for i in range(int(input('Number of students: '))):
    l=[int(input('Enter roll: '))]
    l.append(int(input('Enter age of roll '+str(l[0])+':')))
    l.append(input('Enter name of roll '+str(l[0])+':'))
    list.append(l)
dump(list,f)

f.seek(0,0)
data=load(f)
for record in data:
    if record[1]>16:
        print(record)
f.close()

```
---

### About

This page was made and is maintained by [EccentricX](https://github.com/EccentricX) . Contact him for any bugs or typo in above programs.
