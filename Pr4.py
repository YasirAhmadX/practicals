'''<yasir_ahmad>
WAP to enter 'n' no. of students's information in the form of list of tuple where each tuple consists of roll no. and its corresponding
name. Eg:- [(1,'adya'),(2,'abhinav'),.......(roll,'name')]

Sort the records in ascending order by using bubble sort with respect to their corresponding roll nummbers.
'''

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
