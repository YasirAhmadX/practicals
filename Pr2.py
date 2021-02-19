'''<yasir_ahmad>
WAP to create a list with 'n' number of items where each item refers a tuple which consist of the data as given below:
list=[('aman',45,52,62,52,63),('rahul',52,21,20,25,56),.......(stud_name,mark1,mark2,mark3,mark4,mark5)]

Find the details of those students who is securing more than 65% as their average and display the total count of such students.
'''
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
