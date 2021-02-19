'''<yasir_ahmad>
WAP to enter 'n' no. of students's information in the form of list of tuple where each tuple consists of roll no. and its corresponding
name.Eg:-[(1,'adya'),(2,'abhinav'),.......(roll,'name')]. Write a menu driven choice for the keys 1 and 2, where 1 is used to sequential search and 2 for binary search.
Ask a roll number from the user and search the desired information accordingly.

'''
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
